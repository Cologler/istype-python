#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import INSTANCECHECK, ISA
from collections.abc import Collection

def instancecheck(self, obj, **kwargs):
    if not isinstance(obj, Collection):
        return False
    typ, = self.__args__
    return not kwargs.get('check_item') or all(ISA(x, typ) for x in obj)
INSTANCECHECK[typing.Collection] = instancecheck
