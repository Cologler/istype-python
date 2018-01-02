#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import ISA

@ISA.register(typing.TypeVar)
def instancecheck(self, obj, **kwargs):
    args = self.__constraints__
    if args:
        return ISA(obj, args)
    if self.__covariant__:
        raise NotImplementedError
    if self.__contravariant__:
        raise NotImplementedError
    typevar_table = kwargs.get('typevar_table')
    if isinstance(typevar_table, dict):
        typed = typevar_table.get(self.__name__, None)
        if typed is None:
            typevar_table[self.__name__] = type(obj)
            return True
        else:
            return ISA(obj, typed)
    return True
