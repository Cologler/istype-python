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
from typing_instancecheck import (
    install_all,
    install_generic
)
install_all()
install_generic(True)
from typing import (
    Union,
    Any,
    Optional,
    Tuple,
    List,
    AnyStr,
    Set,
    Dict
)

class Test(unittest.TestCase):
    def test_union(self):
        self.assertTrue(isinstance(1, Union[int]))
        self.assertTrue(isinstance(1, Union[int, str]))
        self.assertTrue(isinstance(1, Union[int, Union[float, str]]))

    def test_any(self):
        self.assertTrue(isinstance(1, Any))

    def test_optional(self):
        self.assertTrue(isinstance('1', Optional[str]))
        self.assertTrue(isinstance(None, Optional[str]))
        self.assertFalse(isinstance(1, Optional[str]))

    def test_tuple(self):
        self.assertTrue(isinstance((1, '1'), Tuple[int, str]))
        self.assertFalse(isinstance((1, 1), Tuple[int, str]))

    def test_list(self):
        self.assertTrue(isinstance([], List[int]))
        self.assertTrue(isinstance([1, 1], List[int]))
        self.assertFalse(isinstance([1, '1'], List[int]))
        self.assertTrue(isinstance([1, '1'], List[object]))

    def test_anystr(self):
        self.assertFalse(isinstance([1, '1'], AnyStr))
        self.assertTrue(isinstance('1', AnyStr))
        self.assertTrue(isinstance(b'1', AnyStr))

    def test_set(self):
        self.assertFalse(isinstance(set([1, '2']), Set[int]))
        self.assertTrue(isinstance(set([1, 2]), Set[int]))

    def test_dict(self):
        self.assertFalse(isinstance({'2': 1}, Dict[int, str]))
        self.assertTrue(isinstance({1: '2'}, Dict[int, str]))


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
