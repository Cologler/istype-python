# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def test_example_global_isinstanceof():
    from typing import Union
    from istype import isinstanceof

    assert isinstanceof(1, Union[int, str])

def test_example_configurable():
    from typing import List
    from istype import TypeMatcher

    matcher = TypeMatcher()
    assert not matcher.isinstance([1], List[str])
    matcher.check_list_elements = False
    assert matcher.isinstance([1], List[str])
