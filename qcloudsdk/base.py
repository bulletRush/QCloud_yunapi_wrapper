#!/usr/bin/env python


class BaseModule(object):
    def __init__(self, engine):
        self.engine = engine


class BaseMonitorDimension(object):
    def __init__(self, kwargs):
        kwargs.pop("self", 0)
        self.kwargs = kwargs

    def to_list(self):
        l = []
        for k, v in self.kwargs.items():
            l.append({"name": k, "value": v})
        return l
