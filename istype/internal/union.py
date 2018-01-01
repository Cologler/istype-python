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
    return ISA(obj, self.__args__)
INSTANCECHECK[type(typing.Union)] = instancecheck
