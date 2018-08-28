# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Optional, Union

from istype import isinstanceof

def test_optional():
    assert isinstanceof('1', Optional[str])
    assert isinstanceof(None, Optional[str])
    assert not isinstanceof(1, Optional[str])

def test_optional_with_union():
    assert isinstanceof('1', Optional[Union[str, int]])
    assert isinstanceof(1, Optional[Union[str, int]])
    assert isinstanceof(None, Optional[Union[str, int]])
    assert not isinstanceof(1.1, Optional[Union[str, int]])
