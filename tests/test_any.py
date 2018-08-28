# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Any, AnyStr

from istype import isinstanceof

def test_any():
    assert isinstanceof(None, Any)
    assert isinstanceof(1, Any)
    assert isinstanceof('1', Any)

def test_anystr():
    assert not isinstanceof(None, AnyStr)
    assert not isinstanceof([1, '1'], AnyStr)
    assert isinstanceof('1', AnyStr)
    assert isinstanceof(b'1', AnyStr)
