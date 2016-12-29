#!/usr/bin/env python
# -*- coding: utf-8 -*-
from qcloudsdk import (
    CbsStorageType, CbsInquiryPriceType, ZoneId, Region, Response
)

from config import engine

# list all portable disk in guangzhou 3
rsp = engine.cbs.describe_cbs_storages(zoneId=ZoneId.GZ3, portable=1)  # type: Response

if rsp.code == 0:
    print "total portable cbs count in GZ3: {0}".format(rsp.data["totalCount"])
    for item in rsp.data["storageSet"]:
        print "\t", item["storageId"], item["storageType"], item["storageSize"]
else:
    # print rsp
    print "some error happened: {0}, {1}, {2}".format(rsp.code, rsp.codeDesc, rsp.message.encode('utf-8'))


# change region to shanghai and list all disk under project '1'
engine.with_region(Region.SH).cbs.describe_cbs_storages(projectId=1)

# switch account
# engine.with_secret(secret_id="<other secret id>", secret_key="<other secret key>")

# close debug log
engine.with_debug(False)

# attach cbs storage
rsp = engine.cbs.attach_cbs_storages(storageIds=["disk-xxx", "disk-yyy"], uInstanceId="ins-aaa")
print rsp

# detach storage
rsp = engine.cbs.detach_cbs_storages(storageIds=["disk-mmm", "disk-nnn"])
print rsp
