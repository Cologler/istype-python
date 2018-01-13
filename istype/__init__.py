#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Iterable
from itertools import zip_longest
from .internal.common import isinstanceof, issubclassof

def match(args: (list, tuple), types: Iterable[type]) -> bool:
    '''
    check whether args match types.

    example:
    ``` py
    `match(('', 1), (str, int)) # True
    ```
    '''

    try:
        if len(args) != len(types):
            return False
    except TypeError:
        # object of type 'types' has no len()
        pass

    empty = object()
    for item, typ in zip_longest(args, types, fillvalue=empty):
        if item is empty or typ is empty:
            return False
        if not isinstanceof(item, typ):
            return False
    return True


__all__ = [
    'isinstanceof',
    'issubclassof',
    'match'
]
