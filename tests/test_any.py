# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Any, AnyStr, ClassVar, Union, List, Optional

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

def test_class_var():
    assert not isinstanceof(None, ClassVar[int])
    assert isinstanceof(1, ClassVar[int])
    assert not isinstanceof(1, ClassVar[str])

def test_union():
    assert isinstanceof(1, Union[int])
    assert isinstanceof(1, Union[int, str])
    assert isinstanceof(1, Union[int, Union[float, str]])

def test_union_complex():
    assert isinstanceof([1], Union[int, List[int]])

def test_optional():
    assert isinstanceof('1', Optional[str])
    assert isinstanceof(None, Optional[str])
    assert not isinstanceof(1, Optional[str])

def test_optional_with_union():
    assert isinstanceof('1', Optional[Union[str, int]])
    assert isinstanceof(1, Optional[Union[str, int]])
    assert isinstanceof(None, Optional[Union[str, int]])
    assert not isinstanceof(1.1, Optional[Union[str, int]])
