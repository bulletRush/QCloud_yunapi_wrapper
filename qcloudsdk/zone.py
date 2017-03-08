#!/usr/bin/env python
# -*- coding=utf-8 -*-
import enum
from base import BaseModule


class Region(enum.Enum):
    BJ = "bj"
    GZ = "gz"
    SH = "sh"
    CA = "ca"
    HK = "hk"
    SG = "sg"
    SHJR = "shjr"
    SZJR = "szjr"
    USW = "usw"


class RegionInt(enum.Enum):
    GZ = 1
    SH = 4
    HK = 5
    CA = 6
    SHJR = 7
    BJ = 8
    SG = 9
    SZJR = 11
    USW = 15


class ZoneId(enum.Enum):
    GZ1 = 100001
    GZ2 = 100002
    GZ3 = 100003
    SH1 = 200001
    HK1 = 300001
    CA1 = 400001
    SHJR1 = 700001
    BJ1 = 800001
    BJ2 = 800002
    SG1 = 900001
    SZJR1 = 110001
    SZJR2 = 110002
    USW1 = 150001


class ZoneModule(BaseModule):
    MODULE_NAME = "cvm"
