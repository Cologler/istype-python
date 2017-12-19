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
    args = self.__constraints__
    if args:
        return ISA(obj, args)
    if self.__covariant__:
        raise NotImplementedError
    if self.__contravariant__:
        raise NotImplementedError
    return True
INSTANCECHECK[typing.TypeVar] = instancecheck
