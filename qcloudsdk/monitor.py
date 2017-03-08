#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class MonitorNamespace(enum.Enum):
    CVM = "qce/cvm"
    DC_LINE = "qce/dc_line"
    CDB = "qce/cdb"


class MonitorMetricName(enum.Enum):
    DISK_USAGE = "disk_usage"
    DISK_READ_TRAFFIC = "disk_read_traffic"
    DISK_WRITE_TRAFFIC = "disk_write_traffic"
    DISK_IO_WAIT = "disk_io_wait"


class MonitorInterface(enum.Enum):
    DESCRIBE_BASE_METRICS = "DescribeBaseMetrics"
    GET_MONITOR_DATA = "GetMonitorData"


class MonitorModule(BaseModule):
    MODULE_NAME = "monitor"

    def describe_base_metrics(
        self, namespace, metricName=None,
    ):
        return self.engine.call(self.MODULE_NAME, MonitorInterface.DESCRIBE_BASE_METRICS, locals())

    def get_monitor_data(
        self, namespace, metricName, dimensions, period=None, startTime=None, endTime=None,
    ):
        return self.engine.call(self.MODULE_NAME, MonitorInterface.GET_MONITOR_DATA, locals())
