#!/usr/bin/env python
import unittest
from qcloudsdk import ZoneId, CbsStorageType, Region
from config import engine


class CbsTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def test_create(self):
        self.engine.with_region(Region.BJ)
        print self.engine.cbs.create_cbs_storages(
            zoneId=ZoneId.BJ1, goodsNum=1, period=1,
            storageType=CbsStorageType.PREMIUM, storageSize=50,
        )


if __name__ == '__main__':
    unittest.main()
