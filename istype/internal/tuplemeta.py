#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import isinstanceof

@isinstanceof.register(typing.TupleMeta)
def instancecheck(self, obj, **kwargs):
    if not isinstance(obj, tuple):
        return False
    return len(obj) == len(self.__args__) and all(isinstance(x, y) for x, y in zip(obj, self.__args__))
