#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import typing
import collections.abc

from .common import TypeMatcher, MatchContext, Router

def union_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    return self.isinstance(obj, type_.__args__, ctx=ctx)

def tuple_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, tuple):
        return False
    if len(obj) != len(type_.__args__):
        return False
    if self.check_tuple_elements:
        if any(not self.isinstance(x, t, ctx=ctx) for x, t in zip(obj, type_.__args__)):
            return False
    return True

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

def collections_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, type_.__origin__):
        return False
    name = type_.__origin__.__name__.lower()
    if getattr(self, f'check_{name}_elements'):
        el_type = type_.__args__[0]
        if any(not self.isinstance(x, el_type, ctx=ctx) for x in obj):
            return False
    return True

def type_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    if not isinstance(obj, type):
        return False
    inner_type, = type_.__args__
    return self.issubclass(obj, inner_type, ctx=ctx)

def class_var_instance_check(self: TypeMatcher, ctx, type_, obj: object):
    inner_type, = type_.__args__
    return self.isinstance(obj, inner_type, ctx=ctx)

if sys.version_info.minor > 6:
    @TypeMatcher.hook_instance_check(typing._GenericAlias)
    @Router
    def generic_alias_route(self: TypeMatcher, ctx: MatchContext, type_, obj: object):
        router: Router = ctx.current_call()
        return router.get(type_.__origin__, self.python_instancecheck)

    # collections
    generic_alias_route.route(list)(collections_instance_check)
    generic_alias_route.route(set)(collections_instance_check)
    generic_alias_route.route(frozenset)(collections_instance_check)
    generic_alias_route.route(collections.abc.Collection)(collections_instance_check)
    generic_alias_route.route(collections.abc.Iterable)(collections_instance_check)

    # mappings
    generic_alias_route.route(dict)(mapping_instance_check)
    generic_alias_route.route(collections.abc.Mapping)(mapping_instance_check)
    generic_alias_route.route(collections.abc.MutableMapping)(mapping_instance_check)

    # tuple
    generic_alias_route.route(tuple)(tuple_instance_check)

    # union
    generic_alias_route.route(typing.Union)(union_instance_check)

    # type
    generic_alias_route.route(type)(type_instance_check)

    # class var
    generic_alias_route.route(typing.ClassVar)(class_var_instance_check)
