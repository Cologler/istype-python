#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
import sys
import traceback
import unittest
from istype import ISA, IS
from typing import (
    Union,
    Any,
    Optional,
    Tuple,
    List,
    AnyStr,
    Set,
    Dict,
    Type,
    Iterable,
    Collection
)

class Test(unittest.TestCase):
    def test_union(self):
        self.assertTrue(ISA(1, Union[int]))
        self.assertTrue(ISA(1, Union[int, str]))
        self.assertTrue(ISA(1, Union[int, Union[float, str]]))

    def test_any(self):
        self.assertTrue(ISA(1, Any))
        self.assertTrue(ISA('1', Any))

    def test_optional(self):
        self.assertTrue(ISA('1', Optional[str]))
        self.assertTrue(ISA(None, Optional[str]))
        self.assertFalse(ISA(1, Optional[str]))

    def test_tuple(self):
        self.assertTrue(ISA((1, '1'), Tuple[int, str]))
        self.assertFalse(ISA((1, 1), Tuple[int, str]))

    def test_list(self):
        self.assertTrue(ISA([], List[int]))
        self.assertTrue(ISA([1, 1], List[int]))
        self.assertTrue(ISA([1, '1'], List[int], check_item=False))
        self.assertFalse(ISA([1, '1'], List[int], check_item=True))
        self.assertTrue(ISA([1, '1'], List[object]))

    def test_anystr(self):
        self.assertFalse(ISA([1, '1'], AnyStr))
        self.assertTrue(ISA('1', AnyStr))
        self.assertTrue(ISA(b'1', AnyStr))

    def test_set(self):
        self.assertTrue(ISA(set([1, '2']), Set[int], check_item=False))
        self.assertFalse(ISA(set([1, '2']), Set[int], check_item=True))
        self.assertTrue(ISA(set([1, 2]), Set[int]))

    def test_dict(self):
        self.assertTrue(ISA({'2': 1}, Dict[int, str], check_item=False))
        self.assertFalse(ISA({'2': 1}, Dict[int, str], check_item=True))
        self.assertTrue(ISA({1: '2'}, Dict[int, str]))

    def test_type(self):
        class User: pass
        class BasicUser(User): pass
        class ProUser(User): pass
        class TeamUser(ProUser): pass
        self.assertTrue(ISA(User, Type[User]))
        self.assertTrue(ISA(BasicUser, Type[User]))
        self.assertTrue(ISA(ProUser, Type[User]))
        self.assertTrue(ISA(TeamUser, Type[User]))
        self.assertFalse(ISA(str, Type[User]))
        self.assertTrue(ISA(str, Type[Any]))

    def test_iterable(self):
        self.assertTrue(ISA([], Iterable[int]))
        self.assertTrue(ISA([1, 1], Iterable[int]))
        self.assertTrue(ISA([1, '1'], Iterable[int], check_item=False))
        self.assertFalse(ISA([1, '1'], Iterable[int], check_item=True))
        self.assertTrue(ISA([1, '1'], Iterable[object]))

    def test_collection(self):
        self.assertTrue(ISA([], Collection[int]))
        self.assertTrue(ISA([1, 1], Collection[int]))
        self.assertTrue(ISA([1, '1'], Collection[int], check_item=False))
        self.assertFalse(ISA([1, '1'], Collection[int], check_item=True))
        self.assertTrue(ISA([1, '1'], Collection[object]))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        unittest.main()
    except Exception:
        traceback.print_exc()
        input()

if __name__ == '__main__':
    main()
