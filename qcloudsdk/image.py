#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class ImageType(enum.Enum):
    PRIVATE = 1
    PUBLIC = 2
    MARKET = 3
    SHARED = 4


class ImageId(enum.Enum):
    CENTOS_5_8 = "img-7br3ouzr"
    CENTOS_7_2 = "img-31tjrtph"
    WINDOWS_2008 = "img-0vbqvzfn"


class ImageModule(BaseModule):
    MODULE_NAME = "image"
