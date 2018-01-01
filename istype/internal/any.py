#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import INSTANCECHECK, SUBCLASSCHECK

def instancecheck(self, obj, **kwargs):
    return True
INSTANCECHECK[type(typing.Any)] = instancecheck

def subclasscheck(self, obj, **kwargs):
    return True
SUBCLASSCHECK[type(typing.Any)] = subclasscheck
