# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .common import TypeMatcher

@TypeMatcher.hook_instance_check(tuple)
def instance_check(self: TypeMatcher, ctx, types, obj: object):
    # tuple mean match any, like `isinstance(1, (str, int))``
    return any(self.isinstance(obj, t, ctx=ctx) for t in types)
