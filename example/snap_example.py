#!/usr/bin/env python
import unittest
from config import engine


class SnapshotTestCase(unittest.TestCase):
    def setUp(self):
        print("\n{0} BEGIN TEST: {1} {2}".format('*' * 20, self._testMethodName, '*' * 20))
        self.engine = engine

    def tearDown(self):
        print("{0} END TEST: {1} {2}\n".format('#' * 20, self._testMethodName, '#' * 20))

    def test_inquiry_price(self):
        print self.engine.snap.inquiry_snapshot_price(
            storageSize=100, zoneId=100003, period=2,
        )

    def test_describe_snap(self):
        print self.engine.snap.describe_snapshots()


if __name__ == '__main__':
    unittest.main()
