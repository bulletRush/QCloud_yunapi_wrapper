#!/usr/bin/env python
import unittest
from qcloudsdk import (
    Region, MonitorNamespace, MonitorMetricName, DiskUsageDimension, DiskReadTrafficDimension,
    DiskIoAwaitDimension, DiskWriteTrafficDimension, DiskSvctmDimension,
    DiskUtilDimension, DiskReadIopsDimension, DiskWriteIopsDimension,
)
from config import engine


class MonitorTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine.with_region(Region.BJ)

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def test_describe_metrics(self):
        print self.engine.monitor.describe_base_metrics(
            namespace=MonitorNamespace.CVM, metricName=MonitorMetricName.DISK_READ_TRAFFIC,
        )

    def test_get_cvm_monitor_data(self):
        print self.engine.with_region(Region.SH)
        cvm_instance_id = "ins-1rr36wrt"
        disk = "root"
        disk_usage_d = DiskUsageDimension(unInstanceId=cvm_instance_id, diskname="vda1")
        disk_read_d = DiskReadTrafficDimension(unInstanceId=cvm_instance_id, disk=disk)
        disk_write_d = DiskWriteTrafficDimension(unInstanceId=cvm_instance_id, disk=disk)
        disk_await_d = DiskIoAwaitDimension(unInstanceId=cvm_instance_id, disk=disk)
        disk_svctm_d = DiskSvctmDimension(unInstanceId=cvm_instance_id, disk=disk)
        disk_util_d = DiskUtilDimension(unInstanceId=cvm_instance_id, disk=disk)
        disk_read_iops_d = DiskReadIopsDimension(unInstanceId=cvm_instance_id, disk=disk)
        disk_write_iops_d = DiskWriteIopsDimension(unInstanceId=cvm_instance_id, disk=disk)
        for d in (
            disk_usage_d, disk_await_d, disk_svctm_d, disk_util_d,
            disk_read_d, disk_write_d, disk_read_iops_d, disk_write_iops_d,
        ):
            print self.engine.monitor.get_monitor_data(dimensions=d)
            print "\n" * 2
            print "/" * 40


if __name__ == '__main__':
    unittest.main()
