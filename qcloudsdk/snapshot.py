#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class CbsSnapShotInterface(enum.Enum):
    CREATE_SNAPSHOT = "CreateSnapshot"
    APPLY_SNAPSHOT = "ApplySnapshot"
    DESCRIBE_SNAPSHOTS = "DescribeSnapshots"
    DELETE_SNAPSHOT = "DeleteSnapshot"
    MODIFY_SNAP_SHOT = "ModifySnapshot"


class SnapModule(BaseModule):
    MODULE_NAME = "snapshot"

    def create_snapshot(
            self, storageId, snapshotName=None
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.CREATE_SNAPSHOT, locals())

    def rollback_snapshot(
            self, snapshotId, storageId
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.APPLY_SNAPSHOT, locals())

    def describe_snapshots(
            self, storageIds,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.DESCRIBE_SNAPSHOTS, locals())

    def delete_snapshot(
            self, snapshotIds,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.DELETE_SNAPSHOT, locals())

    def modify_snapshot(
            self, snapshotId, snapshotName=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.MODIFY_SNAP_SHOT, locals())

