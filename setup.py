#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
from setuptools import setup, find_packages

VERSION = '0.2.0'
DESCRIPTION = ''

long_description = None

if os.path.isfile('README.md'):
    with open('README.md') as f:
        long_description = f.read()

long_description = long_description or DESCRIPTION

setup(
    name = 'istype',
    version = VERSION,
    description = DESCRIPTION,
    long_description = long_description or DESCRIPTION,
    classifiers = [],
    keywords = ['python', 'typing'],
    author = 'cologler',
    author_email='skyoflw@gmail.com',
    url = 'https://github.com/Cologler/istype-python',
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [],
    entry_points = {},
)
