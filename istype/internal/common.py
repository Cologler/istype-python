#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

class MatchContext:
    def __init__(self):
        self._type_vars = None

    @property
    def type_vars(self):
        if self._type_vars is None:
            self._type_vars = {}
        return self._type_vars


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
        return checker(self, ctx, types, obj)

    def issubclass(self, obj: object, types: tuple, *, ctx=None):
        types_cls = type(types)
        checker = self._SUBCLASSCHECK_HOOKS.get(types_cls, TypeMatcher.python_subclasscheck)
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
