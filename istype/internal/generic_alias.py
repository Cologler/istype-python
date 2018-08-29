#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections.abc

from .common import TypeMatcher, MatchContext, Router

@TypeMatcher.hook_instance_check(typing._GenericAlias)
@Router
def generic_alias_instance_check(self: TypeMatcher, ctx: MatchContext, type_, obj: object):
    router: Router = ctx.current_call()
    return router.get(type_.__origin__, self.python_instancecheck)

@generic_alias_instance_check.route(typing.Union)
def union_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    return self.isinstance(obj, type_.__args__, ctx=ctx)

@generic_alias_instance_check.route(tuple)
def tuple_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, tuple):
        return False
    if len(obj) != len(type_.__args__):
        return False
    if self.check_tuple_elements:
        if any(not self.isinstance(x, t, ctx=ctx) for x, t in zip(obj, type_.__args__)):
            return False
    return True

@generic_alias_instance_check.route(dict)
@generic_alias_instance_check.route(collections.abc.Mapping)
@generic_alias_instance_check.route(collections.abc.MutableMapping)
def mapping_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, type_.__origin__):
        return False
    name = type_.__origin__.__name__.lower()
    if getattr(self, f'check_{name}_elements'):
        k_type, v_type = type_.__args__
        for k, v in obj.items():
            if not self.isinstance(k, k_type, ctx=ctx):
                return False
            if not self.isinstance(v, v_type, ctx=ctx):
                return False
    return True

@generic_alias_instance_check.route(list)
@generic_alias_instance_check.route(set)
@generic_alias_instance_check.route(frozenset)
@generic_alias_instance_check.route(collections.abc.Collection)
@generic_alias_instance_check.route(collections.abc.Iterable)
def collections_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, type_.__origin__):
        return False
    name = type_.__origin__.__name__.lower()
    if getattr(self, f'check_{name}_elements'):
        el_type = type_.__args__[0]
        if any(not self.isinstance(x, el_type, ctx=ctx) for x in obj):
            return False
    return True

@generic_alias_instance_check.route(type)
def type_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, type):
        return False
    inner_type, = type_.__args__
    return self.issubclass(obj, inner_type, ctx=ctx)

@generic_alias_instance_check.route(typing.ClassVar)
def class_var_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    inner_type, = type_.__args__
    return self.isinstance(obj, inner_type, ctx=ctx)
