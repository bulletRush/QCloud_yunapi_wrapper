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
    INQUIRY_SNAP_PRICE = "InquirySnapshotPrice"
    # ASP
    DESCRIBE_AUTO_SNAPSHOT_POLICYS = "DescribeAutoSnapshotPolicies"
    DELETE_AUTO_SNAPSHOT_POLICYS = "DeleteAutoSnapshotPolicies"
    MODIFY_AUTO_SNAPSHOT_POLICY = "ModifyAutoSnapshotPolicy"
    BIND_AUTO_SNAPSHOT_POLICY = "BindAutoSnapshotPolicy"
    UNBIND_AUTO_SNAPSHOT_POLICY = "UnbindAutoSnapshotPolicy"
    DESCRIBE_CBS_ASSOCIATED_ASP = "DescribeCbsAssociatedAsp"


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
            self, storageIds=None, snapshotIds=None, searchValue=None,
            offset=None, limit=None,
            zoneId=None, projectIds=None, projectId=None,
            diskType=None, storageTypes=None, snapshotStatus=None,
            order=None, orderBy=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.DESCRIBE_SNAPSHOTS, locals())

    def delete_snapshot(
            self, snapshotIds,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.DELETE_SNAPSHOT, locals())

    def modify_snapshot(
            self, snapshotId, snapshotName=None, isPermanent=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.MODIFY_SNAP_SHOT, locals())

    def inquiry_snapshot_price(
            self, storageSize, zoneId, period, projectId=None, goodsNum=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.INQUIRY_SNAP_PRICE, locals())

    def describe_auto_snapshot_policys(
            self,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.DESCRIBE_AUTO_SNAPSHOT_POLICYS, locals())

    def delete_auto_snapshot_policys(
            self, aspIds,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.DELETE_AUTO_SNAPSHOT_POLICYS, locals())

    def modify_auto_snapshot_policy(
            self, aspId, policy=None, isActivated=None, aspName=None,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.MODIFY_AUTO_SNAPSHOT_POLICY, locals())

    def bind_auto_snapshot_policy(
            self, aspId, cbsIds,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.BIND_AUTO_SNAPSHOT_POLICY, locals())

    def unbind_auto_snapshot_policy(
            self, cbsIds, aspId,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.UNBIND_AUTO_SNAPSHOT_POLICY, locals())

    def describe_cbs_associated_asp(
            self, storageId,
    ):
        return self.engine.call(self.MODULE_NAME, CbsSnapShotInterface.DESCRIBE_CBS_ASSOCIATED_ASP, locals())
