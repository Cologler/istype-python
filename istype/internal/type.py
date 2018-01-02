#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import ISA, IS

@ISA.register(typing.Type)
def instancecheck(self, obj, **kwargs):
    if not isinstance(obj, type):
        return False
    typ, = self.__args__
    return IS(obj, typ)
