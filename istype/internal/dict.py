#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import INSTANCECHECK, ISA

def instancecheck(self, obj, **kwargs):
    if not isinstance(obj, dict):
        return False
    kt, vt = self.__args__
    return not kwargs.get('check_item') or all(ISA(k, kt) for k in obj.keys()) and all(ISA(v, vt) for v in obj.values())
INSTANCECHECK[typing.Dict] = instancecheck
