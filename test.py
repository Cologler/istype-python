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
    T,
    Callable
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

    def _get_ls(self):
        yield []                # 0
        yield [1, '1']          # 1
        yield ['1', 1]          # 2
        yield [1, 1]            # 3

    def test_list(self):
        ''' test iterable, list, collection. '''
        for i, ls in enumerate(self._get_ls()):
            self.assertTrue(isinstanceof(ls, list))

            for gt in (List, Iterable, Collection):
                self.assertTrue(isinstanceof(ls, gt[object]))
                if i in (1, 2):
                    self.assertFalse(isinstanceof(ls, gt[int]))
                elif i == 3:
                    self.assertTrue(isinstanceof(ls, gt[int]))

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

    def test_callable(self):
        def func0(arg1): pass
        self.assertTrue(isinstanceof(func0, Callable))

        def func1(arg1: str, arg2: int) -> int: pass
        self.assertTrue(isinstanceof(func1, Callable))
        self.assertTrue(isinstanceof(func1, Callable[[str, int], int]))
        self.assertFalse(isinstanceof(func1, Callable[[str, str], int]))

        def func2(arg1: (str, int), arg2: int) -> int: pass
        self.assertTrue(isinstanceof(func2, Callable[[str, int], int]))

    def test_callable_covariant(self):
        class A: pass
        class B: pass
        class C(B): pass
        class D(C): pass

        def func1(arg1: A, arg2: B) -> C:
            pass

        self.assertTrue(isinstanceof(func1, Callable[[A, B], C]))
        self.assertFalse(isinstanceof(func1, Callable[[A, A], C]))

        def func2(arg1: C):
            pass

        self.assertFalse(isinstanceof(func2, Callable[[B], None]))
        self.assertTrue(isinstanceof(func2, Callable[[C], None]))
        self.assertTrue(isinstanceof(func2, Callable[[D], None]))

        def func3(arg1: (C, B)):
            pass

        self.assertTrue(isinstanceof(func3, Callable[[B], None]))
        self.assertTrue(isinstanceof(func3, Callable[[C], None]))
        self.assertTrue(isinstanceof(func3, Callable[[D], None]))

        def func4() -> C:
            pass

        self.assertTrue(isinstanceof(func4, Callable[[], B]))
        self.assertTrue(isinstanceof(func4, Callable[[], C]))
        self.assertFalse(isinstanceof(func4, Callable[[], D]))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        unittest.main()
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    main()
