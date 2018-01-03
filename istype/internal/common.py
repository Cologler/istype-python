#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import functools
import collections.abc as abccol

_INSTANCECHECK = {}
_SUBCLASSCHECK = {}

null = object()

def py_instancecheck(self, obj, **kwargs):
    return isinstance(obj, self)

def py_subclasscheck(self, obj, **kwargs):
    return issubclass(obj, self)


def _register(d, *args):
    callback = None
    if len(args) == 1:
        cls, = args
    elif len(args) == 2:
        cls, callback = args
    else:
        raise ValueError
    def r(cb):
        d[cls] = cb
        return cb
    if callback is None:
        return r
    else:
        r(callback)
        return callback

def isinstanceof(x, types: tuple, *,
        typevar_table: typing.Dict[str, type]=None):
    '''
    same as `isinstance()` in python.
    but this function is support the type in `typing`.
    '''
    kwargs = dict(
        typevar_table=typevar_table
    )
    if isinstance(types, tuple):
        return any(isinstanceof(x, t, **kwargs) for t in types)
    cls = getattr(types, '__class__', null)
    return _INSTANCECHECK.get(cls, py_instancecheck)(types, x, **kwargs)
isinstanceof.register = functools.partial(_register, _INSTANCECHECK)


def issubclassof(x, types, *,
        typevar_table: typing.Dict[str, type]=None):
    '''
    same as `issubclass()` in python.
    but this function is support the type in `typing`.
    '''
    if isinstance(types, tuple):
        return any(issubclassof(x, t) for t in types)
    cls = getattr(types, '__class__', null)
    return _SUBCLASSCHECK.get(cls, py_subclasscheck)(types, x)
issubclassof.register = functools.partial(_register, _SUBCLASSCHECK)

# generic collection check:

_INSTANCECHECK_COLLECTION_TYPE_MAP = {
    typing.List: list,
    typing.Set: set,
    typing.FrozenSet: frozenset,
    typing.Collection: abccol.Collection,
    typing.Iterable: abccol.Iterable,
}

@isinstanceof.register(typing.GenericMeta)
def genericmeta_instancecheck(self, obj, **kwargs):
    gorg = getattr(self, '_gorg', null)
    func = _INSTANCECHECK.get(gorg, null)
    if func is not null:
        return func(self, obj, **kwargs)
    coltype = _INSTANCECHECK_COLLECTION_TYPE_MAP.get(gorg, null)
    if coltype is not null:
        if not isinstance(obj, coltype):
            return False
        typ, = self.__args__
        return all(isinstanceof(x, typ, **kwargs) for x in obj)
    return py_instancecheck(self, obj, **kwargs)
