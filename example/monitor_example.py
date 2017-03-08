#!/usr/bin/env python
import unittest
from qcloudsdk import Region, MonitorNamespace, MonitorMetricName
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

    def test_get_monitor_data(self):
        print self.engine.monitor.get_monitor_data(
            namespace=MonitorNamespace.CVM, metricName=MonitorMetricName.DISK_READ_TRAFFIC,
            dimensions=[{"name": "unInstanceId", "value": "ins-13s7bco9"}]
        )

if __name__ == '__main__':
    unittest.main()
