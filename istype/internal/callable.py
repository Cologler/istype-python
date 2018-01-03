#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import inspect
from .common import isinstanceof, issubclassof

@isinstanceof.register(typing.CallableMeta)
def instancecheck(self, obj, **kwargs):
    if not callable(obj):
        return False
    if self.__args__ is not None:
        *args, ret = self.__args__
        sign = inspect.signature(obj)
        if len(sign.parameters) != len(args):
            return False
        for i, p in enumerate(sign.parameters.values()):
            if p.annotation is not sign.empty:
                if not issubclassof(args[i], p.annotation, **kwargs):
                    return False
        if sign.return_annotation is not sign.empty:
            if not issubclassof(sign.return_annotation, ret, **kwargs):
                return False
    return True
