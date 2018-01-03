#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import isinstanceof

@isinstanceof.register(type(typing.Union))
def instancecheck(self, obj, **kwargs):
    return isinstanceof(obj, self.__args__)
