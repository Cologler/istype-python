# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .internal import TypeMatcher

G_TYPE_MATCHER = TypeMatcher()

isinstanceof = G_TYPE_MATCHER.isinstance
issubclassof = G_TYPE_MATCHER.issubclass
