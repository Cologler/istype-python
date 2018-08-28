# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing

from istype import isinstanceof

def test_list():
    assert isinstanceof([], list) is isinstance([], list)

def test_list_generic_empty():
    assert isinstanceof([], typing.List[int])

def test_list_generic():
    assert isinstanceof([1, 1], typing.List[int])
    assert not isinstanceof([1, '1'], typing.List[int])
    assert isinstanceof([1, '1'], typing.List[object])

def test_set():
    assert isinstanceof(set([1, '2']), set)

def test_set_generic():
    assert isinstanceof(set([1, 2]), typing.Set[int])
    assert not isinstanceof(set([1, '2']), typing.Set[int])

def test_dict():
    assert isinstanceof({'2': 1}, dict)

def test_dict_generic():
    assert isinstanceof({1: '2'}, typing.Dict[int, str])
    assert not isinstanceof({'2': 1}, typing.Dict[int, str])

def test_collection_generic_empty():
    assert isinstanceof([], typing.Collection[int])

def test_iterable_generic_empty():
    assert isinstanceof([], typing.Iterable[int])
