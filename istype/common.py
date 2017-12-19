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
    try:
        return isinstance(obj, self)
    except TypeError:
        print('crash self={}, obj={}'.format(self, obj))
        raise

def py_subclasscheck(self, obj, **kwargs):
    try:
        return issubclass(obj, self)
    except TypeError:
        print('crash self={}, obj={}'.format(self, obj))
        raise

def ISA(x, types: tuple, check_item=False):
    '''
    same as `isinstance()` in python.
    but this function is support the type in `typing`.

    if `check_item` is `True`, will check each item from collection (if is).
    '''
    if types is tuple:
        return any(ISA(x, t, check_item) for t in types)
    #if not isinstance(types, type):
    #    raise TypeError('isa() arg 2 must be a type or tuple of types')
    cls = getattr(types, '__class__', null)
    return INSTANCECHECK.get(cls, py_instancecheck)(types, x, check_item=check_item)


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
        return not kwargs.get('check_item') or all(ISA(x, typ) for x in obj)
    return py_instancecheck(self, obj, **kwargs)
INSTANCECHECK[typing.GenericMeta] = genericmeta_instancecheck
