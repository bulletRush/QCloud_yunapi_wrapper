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
    SH2 = 200002
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


class RegionConfig(object):
    def __init__(self, s, id_, zone_id_list):
        self.region = s
        self.region_id = id_
        self.zone_id_list = zone_id_list


gz = RegionConfig(Region.GZ, RegionInt.GZ, (ZoneId.GZ1, ZoneId.GZ2, ZoneId.GZ3))
sh = RegionConfig(Region.SH, RegionInt.SH, (ZoneId.SH1, ZoneId.SH2, ))
bj = RegionConfig(Region.BJ, RegionInt.BJ, (ZoneId.BJ1, ZoneId.BJ2, ))
shjr = RegionConfig(Region.SHJR, RegionInt.SHJR, (ZoneId.SHJR1, ))
szjr = RegionConfig(Region.SZJR, RegionInt.SZJR, (ZoneId.SZJR1, ZoneId.SZJR2, ))
ca = RegionConfig(Region.CA, RegionInt.CA, (ZoneId.CA1, ))
sg = RegionConfig(Region.SG, RegionInt.SG, (ZoneId.SG1, ))
hk = RegionConfig(Region.HK, RegionInt.HK, (ZoneId.HK1, ))
usw = RegionConfig(Region.USW, RegionInt.USW, (ZoneId.USW1, ))

big_region_list = (gz, sh, bj)
small_region_list = (hk, ca, sg, usw)
jr_region_list = (szjr, shjr)
all_region_list = (gz, sh, bj, hk, ca, sg, usw, szjr, shjr)

REGION_MAP = {
    "all": all_region_list,
    "big": big_region_list,
    "small": small_region_list,
    "jr": jr_region_list,
}

for r in all_region_list:
    if isinstance(r.region, enum.Enum):
        s = r.region.value.lower()
    else:
        s = r.region.lower()
    REGION_MAP[s] = (r, )


def get_region_list(l="all"):
    if l in REGION_MAP:
        return REGION_MAP[l]
    else:
        l = l.split(",")
        region_list = []
        for i in l:
            region_list.append(REGION_MAP[i])
        return region_list
