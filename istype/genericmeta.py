#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import INSTANCECHECK, py_instancecheck

def instancecheck(self, obj, **kwargs):
    null = object()
    gorg = getattr(self, '_gorg', null)
    return INSTANCECHECK.get(gorg, py_instancecheck)(self, obj, **kwargs)
INSTANCECHECK[typing.GenericMeta] = instancecheck
