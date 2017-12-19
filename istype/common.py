#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing

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
