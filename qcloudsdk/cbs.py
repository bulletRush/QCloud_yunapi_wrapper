#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class CbsInterface(enum.Enum):
    INQUIRY_PRICE = "InquiryStoragePrice"
    CREATE_CBS_STORAGES = "CreateCbsStorages"
    ATTACH_CBS_STORAGES = "AttachCbsStorages"
    DETACH_CBS_STORAGES = "DetachCbsStorages"
    DESCRIBE_CBS_STORAGES = "DescribeCbsStorages"
    DESCRIBE_CBS_STORAGES_FOR_RECYCLE = "DescribeCbsStoragesForRecycle"
    RESIZE_CBS_STORAGE = "ResizeCbsStorage"
    RENEW_CBS_STORAGE = "RenewCbsStorage"
    DESCRIBE_INSTANCES_CBS_NUM = "DescribeInstancesCbsNum"


class CbsInquiryPriceType(enum.Enum):
    RENEW = "renew"
    CREATE = "create"
    RESIZE = "resize"


class CbsStorageType(enum.Enum):
    SATA = "cloudBasic"
    SSD = "cloudSSD"
    PREMIUM = "cloudPremium"


class CbsPayMode(enum.Enum):
    PREPAY = "prePay"


class CbsModule(BaseModule):
    MODULE_NAME = "cbs"

    def inquiry_storage_price(
            self, inquiryType, storageSize=None, storageType=None, payMode=None, period=None,
            goodsNum=None, storageId=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.INQUIRY_PRICE, locals())

    def create_cbs_storages(
            self, zoneId, goodsNum, period, storageType,
            storageSize=None, projectId=None, snapshotId=None
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.CREATE_CBS_STORAGES, locals())

    def resize_cbs_storage(
            self, storageId, storageSize,
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.RESIZE_CBS_STORAGE, locals())

    def renew_cbs_storage(
            self, storageId, period,
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.RENEW_CBS_STORAGE, locals())

    def attach_cbs_storages(
            self, storageIds, uInstanceId
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.ATTACH_CBS_STORAGES, locals())

    def detach_cbs_storages(
            self, storageIds,
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.DETACH_CBS_STORAGES, locals())

    def describe_cbs_storage_for_recycle(
            self, storageIds=None, offset=None, limit=None, zoneId=None, projectId=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.DESCRIBE_CBS_STORAGES_FOR_RECYCLE, locals())

    def describe_cbs_storages(
            self, storageIds=None, offset=None, limit=None, zoneId=None, projectId=None, diskType=None,
            payMode=None, portable=None, storageType=None, uInstanceIds=None, storageTypes=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.DESCRIBE_CBS_STORAGES, locals())

    def describe_instances_cbs_num(
            self, uInstanceIds,
    ):
        return self.engine.call(self.MODULE_NAME, CbsInterface.DESCRIBE_INSTANCES_CBS_NUM, locals())
