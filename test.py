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
from istype import isinstanceof, issubclassof
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
    Collection,
    T
)

class Test(unittest.TestCase):
    def test_union(self):
        self.assertTrue(isinstanceof(1, Union[int]))
        self.assertTrue(isinstanceof(1, Union[int, str]))
        self.assertTrue(isinstanceof(1, Union[int, Union[float, str]]))

    def test_any(self):
        self.assertTrue(isinstanceof(1, Any))
        self.assertTrue(isinstanceof('1', Any))

    def test_optional(self):
        self.assertTrue(isinstanceof('1', Optional[str]))
        self.assertTrue(isinstanceof(None, Optional[str]))
        self.assertFalse(isinstanceof(1, Optional[str]))

    def test_tuple(self):
        self.assertTrue(isinstanceof((1, '1'), Tuple[int, str]))
        self.assertFalse(isinstanceof((1, 1), Tuple[int, str]))

    def test_list(self):
        self.assertTrue(isinstanceof([1, '1'], list))
        self.assertTrue(isinstanceof([1, 1], List[int]))
        self.assertFalse(isinstanceof([1, '1'], List[int]))
        self.assertTrue(isinstanceof([1, '1'], List[object]))

    def test_anystr(self):
        self.assertFalse(isinstanceof([1, '1'], AnyStr))
        self.assertTrue(isinstanceof('1', AnyStr))
        self.assertTrue(isinstanceof(b'1', AnyStr))

    def test_set(self):
        self.assertTrue(isinstanceof(set([1, '2']), set))
        self.assertFalse(isinstanceof(set([1, '2']), Set[int]))
        self.assertTrue(isinstanceof(set([1, 2]), Set[int]))

    def test_dict(self):
        self.assertTrue(isinstanceof({'2': 1}, dict))
        self.assertFalse(isinstanceof({'2': 1}, Dict[int, str]))
        self.assertTrue(isinstanceof({1: '2'}, Dict[int, str]))

    def test_type(self):
        class User: pass
        class BasicUser(User): pass
        class ProUser(User): pass
        class TeamUser(ProUser): pass
        self.assertTrue(isinstanceof(User, Type[User]))
        self.assertTrue(isinstanceof(BasicUser, Type[User]))
        self.assertTrue(isinstanceof(ProUser, Type[User]))
        self.assertTrue(isinstanceof(TeamUser, Type[User]))
        self.assertFalse(isinstanceof(str, Type[User]))
        self.assertTrue(isinstanceof(str, Type[Any]))

    def test_iterable(self):
        self.assertTrue(isinstanceof([], Iterable[int]))
        self.assertTrue(isinstanceof([1, 1], Iterable[int]))
        self.assertTrue(isinstanceof([1, '1'], list))
        self.assertFalse(isinstanceof([1, '1'], Iterable[int]))
        self.assertTrue(isinstanceof([1, '1'], Iterable[object]))

    def test_collection(self):
        self.assertTrue(isinstanceof([], Collection[int]))
        self.assertTrue(isinstanceof([1, 1], Collection[int]))
        self.assertTrue(isinstanceof([1, '1'], list))
        self.assertFalse(isinstanceof([1, '1'], Collection[int]))
        self.assertTrue(isinstanceof([1, '1'], Collection[object]))

    def test_typevar(self):
        self.assertTrue(isinstanceof([1], List[T], typevar_table={'T': int}))
        self.assertFalse(isinstanceof([str], List[T], typevar_table={'T': int}))

    def test_typevar_buildtable(self):
        # case 1
        table = {}
        self.assertFalse(isinstanceof([1, '1'], List[T], typevar_table=table))
        self.assertTrue(len(table) == 1)
        for k in table:
            v = table[k]
            self.assertEqual(k, 'T')
            self.assertEqual(v, int)

        # case 2
        table = {}
        self.assertTrue(isinstanceof([1, 1], List[T], typevar_table=table))
        self.assertTrue(len(table) == 1)
        for k in table:
            v = table[k]
            self.assertEqual(k, 'T')
            self.assertEqual(v, int)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        unittest.main()
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    main()
