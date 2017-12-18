#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing

def install_union():
    def instancecheck(self, obj):
        return isinstance(obj, self.__args__)
    typing._Union.__instancecheck__ = instancecheck

def install_any():
    def instancecheck(self, obj):
        return True
    typing._Any.__instancecheck__ = instancecheck

def install_tuple():
    def instancecheck(self, obj):
        if not isinstance(obj, tuple):
            return False
        if len(obj) != len(self.__args__):
            return False
        for x, y in zip(obj, self.__args__):
            if not isinstance(x, y):
                return False
        return True
    typing.TupleMeta.__instancecheck__ = instancecheck

def install_generic(check_each_item=False):
    '''
    base type for:
    * List
    * Set
    * Dict
    '''
    rawfunc = typing.GenericMeta.__instancecheck__
    type_map = {
        typing.List: list,
        typing.Set: set,
        typing.Dict: dict
    }
    empty = object()
    def instancecheck(self, obj):
        itype = type_map.get(self._gorg)
        if itype is None:
            return rawfunc(self, obj)
        if not isinstance(obj, itype):
            return False
        if check_each_item and obj:
            args = self.__args__
            if len(args) == 1:
                typ = args[0]
                for x in obj:
                    if not isinstance(x, typ):
                        return False
            elif len(args) == 2: # dict
                kt, vt = args
                for k in obj.keys():
                    if not isinstance(k, kt):
                        return False
                for v in obj.values():
                    if not isinstance(v, vt):
                        return False
        return True
    typing.GenericMeta.__instancecheck__ = instancecheck

def install_typevar():
    def instancecheck(self, obj):
        if self.__covariant__ or self.__contravariant__:
            raise NotImplementedError
        args = self.__constraints__
        if args:
            return isinstance(obj, args)
        return True
    typing.TypeVar.__instancecheck__ = instancecheck

def install_all():
    ''' install all '''
    install_union()
    install_any()
    install_tuple()
    install_generic()
    install_typevar()

