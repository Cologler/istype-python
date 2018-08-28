# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def register_to_dict(d: dict):
    '''
    get a decorator for register to a dict.
    '''
    def decorator(key):
        def wrap(func):
            assert key not in d
            d[key] = func
            return func
        return wrap
    return decorator
