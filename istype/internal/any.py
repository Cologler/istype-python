#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import ISA, IS

@ISA.register(type(typing.Any))
def instancecheck(self, obj, **kwargs):
    return True

@IS.register(type(typing.Any))
def subclasscheck(self, obj, **kwargs):
    return True
