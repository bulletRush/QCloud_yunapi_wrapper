#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class ResourceType(enum.Enum):
    CVM = "cvm"
    CBS = "cbs"


class TradeInterface(enum.Enum):
    SET_RENEW_FLAG = "SetRenewFlag"


class TradeModule(BaseModule):
    MODULE_NAME = "trade"

    def set_renew_flag(
        self, uuids, region, type, autoRenewFlag,
    ):
        return self.engine.call(self.MODULE_NAME, TradeInterface.SET_RENEW_FLAG, locals())
