#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
import sys
import binascii
import hashlib
import hmac
import time
import random
import json
import requests
import warnings
from cbs import CbsModule
from snapshot import SnapModule
from ccr import CcrModule
from base import BaseModule
from cvm import CvmModule
from trade import TradeModule
warnings.filterwarnings("ignore")

VERSION = 'SDK_PYTHON_barrettwu_0.1'


class Response(object):
    def __init__(self, rsp):
        """
        :param dict rsp: 调用云API返回的原始参数
        """
        self.code = rsp.pop("code")
        self.message = rsp.pop("message")
        self.codeDesc = rsp.pop("codeDesc")
        self.data = rsp

    def __repr__(self):
        if self.data:
            s = u"<Response: {0}:{1}:{2}:{3}>".format(self.code, self.codeDesc, self.message, self.data)
        else:
            s = u"<Response: {0}:{1}:{2}>".format(self.code, self.codeDesc, self.message)
        return s.encode("utf-8")


def _fix_params(prefix, params):
    d = {}
    if params is None:
        return d
    if isinstance(params, BaseModule):
        return d
    if not isinstance(params, (tuple, list, dict)):
        if isinstance(params, enum.Enum):
            params = params.value
        d[prefix] = params
        return d
    if isinstance(params, (list, tuple)):
        for idx, item in enumerate(params):
            if prefix:
                key = "{0}.{1}".format(prefix, idx)
            else:
                key = "{0}".format(idx)
            d.update(_fix_params(key, item))
        return d
    if isinstance(params, dict):
        for k, v in params.iteritems():
            if prefix:
                key = '{0}.{1}'.format(prefix, k)
            else:
                key = '{0}'.format(k)
            d.update(_fix_params(key, v))
        return d
    raise Exception("fuck and fuck again")


class QCloudEngine(object):
    def __init__(self, secret_id, secret_key, method='get', region='gz', timeout=10, debug=True):
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.method = method.upper()
        self.region = region
        self.timeout = timeout
        self.debug = debug
        self.cbs = CbsModule(self)
        self.snap = SnapModule(self)
        self.ccr = CcrModule(self)
        self.cvm = CvmModule(self)
        self.trade = TradeModule(self)

    def with_secret(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key
        return self

    def with_region(self, region):
        self.region = region
        return self

    def with_method(self, method):
        self.method = method.upper()
        return self

    def with_debug(self, debug=True):
        self.debug = debug
        return self

    def generate_signature(self, component_url, params):
        l = {}
        for k in params:
            if self.method == 'POST' and str(params[k]).startswith("@"):
                continue
            l[k] = params[k]
        raw = self.method + component_url + '?' + '&'.join(
            k.replace('_', ".") + "=" + str(l[k]) for k in sorted(l.keys())
        )
        hashed = hmac.new(self.secret_key, raw, hashlib.sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]

    def fix_params(self, params):
        if not isinstance(params, (dict,)):
            return params
        if 'Region' not in params:
            params['Region'] = self.region
        if 'SecretId' not in params:
            params['SecretId'] = self.secret_id
        if 'Nonce' not in params:
            params['Nonce'] = random.randint(1, sys.maxint)
        if 'Timestamp' not in params:
            params['Timestamp'] = int(time.time())
        if 'RequestClient' not in params:
            params['RequestClient'] = VERSION

        return _fix_params(None, params)

    @staticmethod
    def generate_component_url(component):
        return component + ".api.qcloud.com/v2/index.php"

    def call(self, component, action, params, rsp=None):
        component_url = self.generate_component_url(component)
        params = self.fix_params(params)
        if self.debug:
            print '**** params: {0}\n'.format(params)
        params['Action'] = action
        params['Signature'] = self.generate_signature(component_url, params)
        url = 'https://{0}'.format(component_url)
        if self.method == 'GET':
            req = requests.get(url, params=params, timeout=self.timeout, verify=False)
        else:
            req = requests.post(url, data=params, timeout=self.timeout, verify=False)
        if self.debug:
            print '**** url: {0}\n'.format(req.url)

        if req.status_code != requests.codes.ok:
            req.raise_for_status()
        if self.debug:
            print '**** rsp: {0}\n'.format(req.text)
        ret = json.loads(req.text)
        return Response(ret)
