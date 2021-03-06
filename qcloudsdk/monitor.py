#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule, BaseMonitorDimension


class MonitorNamespace(enum.Enum):
    CVM = "qce/cvm"
    DC_LINE = "qce/dc_line"
    CDB = "qce/cdb"
    CBS = "qce/cbs"


class MonitorMetricName(enum.Enum):
    DISK_READ_TRAFFIC = "disk_read_traffic"
    DISK_WRITE_TRAFFIC = "disk_write_traffic"
    DISK_READ_IOPS = "disk_read_iops"
    DISK_WRITE_IOPS = "disk_write_iops"
    DISK_AWAIT = "disk_await"
    DISK_SVCTM = "disk_svctm"
    DISK_UTIL = "disk_util"
    DISK_USAGE = "disk_usage"


class MonitorInterface(enum.Enum):
    DESCRIBE_BASE_METRICS = "DescribeBaseMetrics"
    GET_MONITOR_DATA = "GetMonitorData"


class DiskUsageDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_USAGE
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, diskname):
        super(DiskUsageDimension, self).__init__(locals())


class DiskReadTrafficDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_READ_TRAFFIC
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, disk):
        super(DiskReadTrafficDimension, self).__init__(locals())


class DiskWriteTrafficDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_WRITE_TRAFFIC
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, disk):
        super(DiskWriteTrafficDimension, self).__init__(locals())


class DiskReadIopsDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_READ_IOPS
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, disk):
        super(DiskReadIopsDimension, self).__init__(locals())


class DiskWriteIopsDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_WRITE_IOPS
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, disk):
        super(DiskWriteIopsDimension, self).__init__(locals())


class DiskIoAwaitDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_AWAIT
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, disk):
        super(DiskIoAwaitDimension, self).__init__(locals())


class DiskSvctmDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_SVCTM
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, disk):
        super(DiskSvctmDimension, self).__init__(locals())


class DiskUtilDimension(BaseMonitorDimension):
    METRIC_NAME = MonitorMetricName.DISK_UTIL
    NAME_SPACE = MonitorNamespace.CVM

    def __init__(self, unInstanceId, disk):
        super(DiskUtilDimension, self).__init__(locals())


class MonitorModule(BaseModule):
    MODULE_NAME = "monitor"

    def describe_base_metrics(
        self, namespace, metricName=None,
    ):
        return self.engine.call(self.MODULE_NAME, MonitorInterface.DESCRIBE_BASE_METRICS, locals())

    def get_monitor_data(
        self, dimensions, namespace=None, metricName=None, period=None, startTime=None, endTime=None,
    ):
        if namespace is None:
            namespace = dimensions.NAME_SPACE
        if metricName is None:
            metricName = dimensions.METRIC_NAME
        return self.engine.call(self.MODULE_NAME, MonitorInterface.GET_MONITOR_DATA, locals())


if __name__ == '__main__':
    x = DiskUsageDimension(unInstanceId="ins-dxxx", diskname="aaa")
