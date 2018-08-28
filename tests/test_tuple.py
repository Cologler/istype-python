# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Tuple

from istype import isinstanceof

def test_tuple():
    assert isinstanceof((1, '1'), Tuple[int, str])
    assert not isinstanceof((1, 1), Tuple[int, str])
