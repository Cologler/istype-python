#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import isinstanceof

@isinstanceof.register(typing.Dict)
def instancecheck(self, obj, **kwargs):
    if not isinstance(obj, dict):
        return False
    kt, vt = self.__args__
    return all(isinstanceof(k, kt) for k in obj.keys()) and all(isinstanceof(v, vt) for v in obj.values())
