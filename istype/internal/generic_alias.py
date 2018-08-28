#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections.abc

from .common import TypeMatcher
from .utils import register_to_dict

_ORIGIN_MAP = {}

register = register_to_dict(_ORIGIN_MAP)

@TypeMatcher.hook_instance_check(typing._GenericAlias)
def generic_alias_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    args = (self, ctx, type_, obj)
    try:
        checker = _ORIGIN_MAP[type_.__origin__]
    except KeyError:
        return self.python_instancecheck(*args)
    return checker(*args)

@register(typing.Union)
def union_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    return self.isinstance(obj, type_.__args__, ctx=ctx)

@register(tuple)
def tuple_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, tuple):
        return False
    if len(obj) != len(type_.__args__):
        return False
    if self.check_tuple_elements:
        if any(not self.isinstance(x, t, ctx=ctx) for x, t in zip(obj, type_.__args__)):
            return False
    return True

@register(dict)
def dict_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, dict):
        return False
    if self.check_dict_elements:
        k_type, v_type = type_.__args__
        for k, v in obj.items():
            if not self.isinstance(k, k_type, ctx=ctx):
                return False
            if not self.isinstance(v, v_type, ctx=ctx):
                return False
    return True

@register(set)
def set_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, set):
        return False
    if self.check_set_elements:
        el_type = type_.__args__[0]
        if any(not self.isinstance(x, el_type, ctx=ctx) for x in obj):
            return False
    return True

@register(list)
def list_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, list):
        return False
    if self.check_list_elements:
        el_type = type_.__args__[0]
        if any(not self.isinstance(x, el_type, ctx=ctx) for x in obj):
            return False
    return True

@register(collections.abc.Collection)
def collection_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, collections.abc.Collection):
        return False
    if self.check_collection_elements:
        el_type = type_.__args__[0]
        if any(not self.isinstance(x, el_type, ctx=ctx) for x in obj):
            return False
    return True

@register(collections.abc.Iterable)
def iterable_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, collections.abc.Iterable):
        return False
    if self.check_iterable_elements:
        el_type = type_.__args__[0]
        if any(not self.isinstance(x, el_type, ctx=ctx) for x in obj):
            return False
    return True

@register(type)
def type_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, type):
        return False
    inner_type, = type_.__args__
    return self.issubclass(obj, inner_type, ctx=ctx)
