#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing

from .common import TypeMatcher

@TypeMatcher.hook_instance_check(type(typing.Any))
def instance_check(*args):
    return True

@TypeMatcher.hook_subclass_check(type(typing.Any))
def subclass_check(*args):
    return True
