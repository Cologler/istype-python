#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing

from .common import TypeMatcher, MatchContext


class TypeVarInfo:
    def __init__(self, type_var):
        self._type_var = type_var
        self._type = None

    def update_type(self, matcher: TypeMatcher, ctx: MatchContext, type_):
        if self._type is not None:
            if type_.__covariant__:
                raise NotImplementedError
            if type_.__contravariant__:
                raise NotImplementedError
        self._type = type_
        return True


@TypeMatcher.hook_instance_check(typing.TypeVar)
def instance_check(self: TypeMatcher, ctx: MatchContext, type_, obj: object):
    args = type_.__constraints__
    if args:
        return self.isinstance(obj, args, ctx=ctx)
    type_vars = ctx.type_vars
    type_var_info = type_vars.get(type_.__name__, None)
    if type_var_info is None:
        type_vars[type_.__name__] = type_var_info = TypeVarInfo(type_)
    type_var_info.update_type(type(obj))
    assert NotImplementedError
