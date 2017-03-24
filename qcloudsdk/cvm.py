#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class CvmInterface(enum.Enum):
    DESCRIBE_INSTANCES = "DescribeInstances"
    RUN_INSTANCES = "RunInstances"
    RUN_INSTANCES_HOUR = "RunInstancesHour"
    INQUIRY_INSTANCE_PRICE = "InquiryInstancePrice"
    RESET_INSTANCES = "ResetInstances"
    DESCRIBE_INSTANCE_DISK_NAMES = "DescribeInstanceDiskNames"


class CvmModule(BaseModule):
    MODULE_NAME = "cvm"

    def describe_instances(
        self, instanceIds=None, lanIps=None, searchWord=None, status=None, projectId=None, zoneId=None, offset=None,
        limit=None,
):
        return self.engine.call(self.MODULE_NAME, CvmInterface.DESCRIBE_INSTANCES, locals())

    def run_instances(
        self, cpu, mem, storageSize, period, imageId, zoneId=None, imageType=None, bandwidthType=None,
):
        return self.engine.call(self.MODULE_NAME, CvmInterface.RUN_INSTANCES, locals())

    def inquiry_instance_price(
            self, instanceType, cpu, mem, period, storageType, storageSize, imageType, imageId,
            goodsNum=None, bandwidth=None, rootSize=None, bandwidthType=None,
    ):
        return self.engine.call(self.MODULE_NAME, CvmInterface.INQUIRY_INSTANCE_PRICE, locals())

    def run_instances_hour(
            self, zoneId,
            cpu, mem,
            imageId, imageType,
            bandwidthType=None, bandwidth=None, wanIp=None,
            storageType=None, storageSize=None, rootSize=None,
    ):
        return self.engine.call(self.MODULE_NAME, CvmInterface.RUN_INSTANCES_HOUR, locals())

    def reset_instances(
            self, instanceId, imageType=None, imageId=None, password=None,
            needSecurityAgent=None, needMonitorAgent=None, rootSize=None,
    ):
        return self.engine.call(self.MODULE_NAME, CvmInterface.RESET_INSTANCES, locals())

    def describe_instance_disk_names(
            self, instanceId
    ):
        return self.engine.call(self.MODULE_NAME, CvmInterface.DESCRIBE_INSTANCE_DISK_NAMES, locals())
