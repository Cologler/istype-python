#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .common import isinstanceof, issubclassof

@isinstanceof.register(tuple)
def instancecheck(self, obj, **kwargs):
    return any(isinstanceof(obj, t, **kwargs) for t in self)

@issubclassof.register(tuple)
def subclasscheck(self, obj, **kwargs):
    return any(issubclassof(obj, t) for t in self)
