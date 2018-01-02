#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import ISA

@ISA.register(type(typing.Union))
def instancecheck(self, obj, **kwargs):
    return ISA(obj, self.__args__)
