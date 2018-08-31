# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import typing

from .common import TypeMatcher, MatchContext, Router
from .generic_alias import (
    collections_instance_check,
    mapping_instance_check,
    tuple_instance_check,
    union_instance_check,
    type_instance_check,
)

if sys.version_info.minor == 6:
    def class_var_instance_check_py36(self: TypeMatcher, ctx, type_, obj: object):
        inner_type = type_.__type__
        return self.isinstance(obj, inner_type, ctx=ctx)

    @TypeMatcher.hook_instance_check(typing.GenericMeta)
    @Router
    def generic_meta_route(self: TypeMatcher, ctx: MatchContext, type_, obj: object):
        router: Router = ctx.current_call()
        return router.get(type_.__origin__, self.python_instancecheck)

    # collections
    generic_meta_route.route(typing.List)(collections_instance_check)
    generic_meta_route.route(typing.Set)(collections_instance_check)
    generic_meta_route.route(typing.FrozenSet)(collections_instance_check)
    generic_meta_route.route(typing.Collection)(collections_instance_check)
    generic_meta_route.route(typing.Iterable)(collections_instance_check)

    # mappings
    generic_meta_route.route(typing.Dict)(mapping_instance_check)
    generic_meta_route.route(typing.Mapping)(mapping_instance_check)
    generic_meta_route.route(typing.MutableMapping)(mapping_instance_check)

    # tuple
    TypeMatcher.hook_instance_check(typing.TupleMeta)(tuple_instance_check)

    # union
    # assert type(typing.Union[int, str]) is not typing.Union
    TypeMatcher.hook_instance_check(type(typing.Union[int, str]))(union_instance_check)

    # type
    generic_meta_route.route(typing.Type)(type_instance_check)

    # class var
    TypeMatcher.hook_instance_check(type(typing.ClassVar[int]))(class_var_instance_check_py36)
