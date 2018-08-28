#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
import importlib

from .common import TypeMatcher

for name in os.listdir(os.path.dirname(__file__)):
    if name.startswith('_') or not name.endswith('.py'):
        continue
    importlib.import_module('.' + name[:-3], __name__)
