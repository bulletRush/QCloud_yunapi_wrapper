#!/usr/bin/env python
import unittest
from qcloudsdk import ZoneId, CbsStorageType, Region, get_region_list, RegionConfig
from config import engine


class CbsTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine.with_region(Region.BJ)

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def test_create(self):
        self.engine.debug = False
        for region in get_region_list():  # type: RegionConfig
            self.engine.with_region(region.region)
            for z in region.zone_id_list:
                print "check:", region.region, z
                print self.engine.cbs.create_cbs_storages(
                    zoneId=z, goodsNum=1, period=1,
                    storageType=CbsStorageType.SSD, storageSize=50,
                )

    def xtest_resize(self):
        print self.engine.cbs.resize_cbs_storage(storageId="disk-o3y0ccya", storageSize=270)

    def xtest_renew(self):
        print self.engine.cbs.renew_cbs_storage(storageId="disk-4kmc04su", period=1)


if __name__ == '__main__':
    unittest.main()
