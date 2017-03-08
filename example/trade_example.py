#!/usr/bin/env python
import unittest
from qcloudsdk import Region, ResourceType
from config import engine


class TradeTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def test_set_auto_renew(self):
        self.engine.with_region(Region.BJ)
        print self.engine.trade.set_renew_flag(
            region=8, uuids=["disk-mod36xfv"], type=ResourceType.CBS, autoRenewFlag=0,
        )


if __name__ == '__main__':
    unittest.main()
