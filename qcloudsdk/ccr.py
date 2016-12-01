#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class RegistryInterface(enum.Enum):
    GET_REPOSITORY_LIST = "GetRepositoryList"
    CREATE_REPOSITORY = "CreateRepository"
    GET_USER_REPOSITORY_LIST = "GetUserRepositoryList"
    GET_USER_INFO = "GetUserInfo"
    GET_NAMESPACE_INFO = "GetNamespaceInfo"
    REGISTER_REPOSITORY_ACCOUNT = "RegisterRepositoryAccount"


class CcrModule(BaseModule):
    MODULE_NAME = "ccr"

    def get_repository_list(
        self, offset=None, limit=None,
    ):
        return self.engine.call(self.MODULE_NAME, RegistryInterface.GET_REPOSITORY_LIST, locals())

    def get_user_repository_list(
            self, reponame=None, limit=None, offset=None,
    ):
        return self.engine.call(self.MODULE_NAME, RegistryInterface.GET_USER_REPOSITORY_LIST, locals())

    def create_repository(
            self, reponame, public, description=None,
    ):
        return self.engine.call(self.MODULE_NAME, RegistryInterface.CREATE_REPOSITORY, locals())

    def get_namespace_info(
        self,
    ):
        return self.engine.call(self.MODULE_NAME, RegistryInterface.GET_NAMESPACE_INFO, locals())

    def get_user_info(
        self,
    ):
        return self.engine.call(self.MODULE_NAME, RegistryInterface.GET_USER_INFO, locals())

    def register_repository_account(
            self, password, namespace,
    ):
        return self.engine.call(self.MODULE_NAME, RegistryInterface.REGISTER_REPOSITORY_ACCOUNT, locals())
