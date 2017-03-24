#!/usr/bin/env python
import unittest
from qcloudsdk import Region
from config import engine


class CvmTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine.with_region(Region.BJ)

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def test_describe_instance_disk_name(self):
        print self.engine.with_region(Region.BJ).cvm.describe_instance_disk_names(instanceId="ins-q7gr39d3")


if __name__ == '__main__':
    unittest.main()
