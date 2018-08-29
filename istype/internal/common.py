#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import contextlib


class MatchContext:
    def __init__(self):
        self._type_vars = None
        self._route_stack = []

    @property
    def type_vars(self):
        if self._type_vars is None:
            self._type_vars = {}
        return self._type_vars

    def then_call(self, func):
        @contextlib.contextmanager
        def _():
            self._route_stack.append(func)
            yield
            self._route_stack.pop()
        return _()

    def current_call(self):
        return self._route_stack[-1]


class TypeMatcher:
    _INSTANCECHECK_HOOKS = {}
    _SUBCLASSCHECK_HOOKS = {}

    def __init__(self):
        self.check_tuple_elements = True
        self.check_list_elements = True
        self.check_collection_elements = True
        self.check_dict_elements = True
        self.check_set_elements = True
        self.check_iterable_elements = False

    @staticmethod
    def python_instancecheck(self, ctx, types: tuple, obj: object):
        return isinstance(obj, types)

    @staticmethod
    def python_subclasscheck(self, ctx, types: tuple, cls: object):
        return issubclass(cls, types)

    def isinstance(self, obj: object, types: tuple, *, ctx=None):
        types_cls = type(types)
        checker = self._INSTANCECHECK_HOOKS.get(types_cls, TypeMatcher.python_instancecheck)
        ctx = ctx or MatchContext()
        with ctx.then_call(checker):
            return checker(self, ctx, types, obj)

    def issubclass(self, obj: object, types: tuple, *, ctx=None):
        types_cls = type(types)
        checker = self._SUBCLASSCHECK_HOOKS.get(types_cls, TypeMatcher.python_subclasscheck)
        ctx = ctx or MatchContext()
        with ctx.then_call(checker):
            return checker(self, ctx, types, obj)

    @classmethod
    def hook_instance_check(cls, type_: type):
        def register(func):
            assert type_ not in cls._INSTANCECHECK_HOOKS
            cls._INSTANCECHECK_HOOKS[type_] = func
            return func
        return register

    @classmethod
    def hook_subclass_check(cls, type_: type):
        def register(func):
            assert type_ not in cls._SUBCLASSCHECK_HOOKS
            cls._SUBCLASSCHECK_HOOKS[type_] = func
            return func
        return register


class Router:
    def __init__(self, func):
        self._func = func
        self._route_paths = {}

    def __call__(self, matcher: TypeMatcher, ctx: MatchContext, type_, obj: object):
        next_call = self._func(matcher, ctx, type_, obj)
        with ctx.then_call(next_call):
            return next_call(matcher, ctx, type_, obj)

    def route(self, key):
        def _(func):
            assert key not in self._route_paths
            self._route_paths[key] = func
            return func
        return _

    def get(self, key, d):
        try:
            return self._route_paths[key]
        except KeyError:
            return d
