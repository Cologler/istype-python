# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Union, List

from istype import isinstanceof

def test_union():
    assert isinstanceof(1, Union[int])
    assert isinstanceof(1, Union[int, str])
    assert isinstanceof(1, Union[int, Union[float, str]])

def test_union_complex():
    assert isinstanceof([1], Union[int, List[int]])
