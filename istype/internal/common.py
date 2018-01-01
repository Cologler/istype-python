#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections.abc as abccol

INSTANCECHECK = {}
SUBCLASSCHECK = {}

null = object()

def py_instancecheck(self, obj, **kwargs):
    return isinstance(obj, self)

def py_subclasscheck(self, obj, **kwargs):
    return issubclass(obj, self)

def ISA(x, types: tuple,
        check_item=False,
        typevar_table: typing.Dict[str, type]=None):
    '''
    same as `isinstance()` in python.
    but this function is support the type in `typing`.

    if `check_item` is `True`, will check each item from collection (if is).
    '''
    if types is tuple:
        return any(ISA(x, t, check_item, typevar_table) for t in types)
    #if not isinstance(types, type):
    #    raise TypeError('isa() arg 2 must be a type or tuple of types')
    cls = getattr(types, '__class__', null)
    return INSTANCECHECK.get(cls, py_instancecheck)(types, x,
        check_item=check_item,
        typevar_table=typevar_table)


def IS(x, types):
    '''
    same as `issubclass()` in python.
    but this function is support the type in `typing`.
    '''
    if types is tuple:
        return any(IS(x, t) for t in types)
    cls = getattr(types, '__class__', null)
    return SUBCLASSCHECK.get(cls, py_subclasscheck)(types, x)


# generic collection check:

INSTANCECHECK_COLLECTION_TYPE_MAP = {
    typing.List: list,
    typing.Set: set,
    typing.FrozenSet: frozenset,
    typing.Collection: abccol.Collection,
    typing.Iterable: abccol.Iterable,
}

def genericmeta_instancecheck(self, obj, **kwargs):
    gorg = getattr(self, '_gorg', null)
    func = INSTANCECHECK.get(gorg, null)
    if func is not null:
        return func(self, obj, **kwargs)
    coltype = INSTANCECHECK_COLLECTION_TYPE_MAP.get(gorg, null)
    if coltype is not null:
        if not isinstance(obj, coltype):
            return False
        typ, = self.__args__
        return not kwargs.get('check_item') or all(ISA(x, typ, **kwargs) for x in obj)
    return py_instancecheck(self, obj, **kwargs)
INSTANCECHECK[typing.GenericMeta] = genericmeta_instancecheck
