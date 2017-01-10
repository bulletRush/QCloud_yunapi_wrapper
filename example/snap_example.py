#!/usr/bin/env python
import unittest
from config import engine
from qcloudsdk import Region, ZoneId


class SnapshotTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine.with_region(Region.CA)

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def test_inquiry_price(self):
        print self.engine.snap.inquiry_snapshot_price(
            storageSize=100, zoneId=ZoneId.CA1, period=2,
        )

    def xtest_describe_snap(self):
        print self.engine.snap.describe_snapshots(
            snapshotIds=["snap-l82l72gl", "snap-ptqv2xmn"],
        )

    def xtest_describe_cbs_associated_asp(self):
        print self.engine.snap.describe_cbs_associated_asp("disk-7nzio4jq")

    def xtest_describe_asp(self):
        print self.engine.snap.describe_auto_snapshot_policys()

    def test_create_asp(self):
        print self.engine.snap.create_auto_snapshot_policies(
            policy=[{"dayOfWeek": ["1", "2"], "hour": ["11"]}], aspName=u"barrettwu测试",
            retentionDays=7, isPermanent=0, isActivated=0,
        )


if __name__ == '__main__':
    unittest.main()
