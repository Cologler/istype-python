#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import isinstanceof, issubclassof

@isinstanceof.register(type(typing.Any))
def instancecheck(self, obj, **kwargs):
    return True

@issubclassof.register(type(typing.Any))
def subclasscheck(self, obj, **kwargs):
    return True
