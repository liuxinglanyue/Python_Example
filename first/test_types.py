#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jiaojianfeng'

import types

x = 20

print type(x) is types.IntType

print x.__class__

print x.__class__ is type(x) is int is types.IntType

y = x

print hex(id(x)), hex(id(y))   #id(object) 获取内存地址

print hex(id(int)), hex(id(types.IntType))