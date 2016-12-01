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


class ZoneId(enum.Enum):
    GZ1 = 100001
    GZ2 = 100002
    GZ3 = 100003
    SH1 = 200001
    HK1 = 300001
    CA1 = 400001
    SHJR1 = 700001
    BJ1 = 800001
    SG1 = 900001
    SZJR1 = 110001
    SZJR2 = 110002


class ZoneModule(BaseModule):
    MODULE_NAME = "cvm"
