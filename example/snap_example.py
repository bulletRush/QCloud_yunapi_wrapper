#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from config import engine
from qcloudsdk import Region, ZoneId


class SnapshotTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine.with_region(Region.BJ)
        self.asp_id_ca = "asp-63nkvfj6"
        self.asp_id_bj = "asp-63nkviwi"
        self.all_policy = [{"dayOfWeek": ["0", "1", "2", "3", "4", "5", "6"], "hour": ["12"]}]

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def xtest_inquiry_price(self):
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

    def xtest_create_asp(self):
        print self.engine.snap.create_auto_snapshot_policies(
            policy=self.all_policy, aspName="barrettwu测试",
            retentionDays=7, isPermanent=0, isActivated=0,
        )

    def xtest_bound_cbs(self):
        print self.engine.snap.bind_auto_snapshot_policy(
            aspId=self.asp_id_bj, storageIdList=["disk-ezwe9uq7", "disk-16gvmvet"]
        )

    def test_modify_asp(self):
        print self.engine.snap.modify_auto_snapshot_policy(
            aspId=self.asp_id_bj, policy=self.all_policy, isActivated=1,
        )

    def xtest_unbound_cbs(self):
        print self.engine.snap.unbind_auto_snapshot_policy(
            aspId=self.asp_id_ca, storageIdList=["disk-ezwe9uq7", "disk-6fnjxyv9", ]
        )

    def xtest_delete_asp(self):
        print self.engine.snap.delete_auto_snapshot_policies(
            aspIds=[self.asp_id_ca],
        )

    def xtest_describe_asp(self):
        print self.engine.snap.describe_auto_snapshot_policies()


if __name__ == '__main__':
    unittest.main()
