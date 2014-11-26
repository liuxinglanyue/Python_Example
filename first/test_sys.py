#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jiaojianfeng'

import sys

x = 0x1234
print sys.getsizeof(x)

print sys.getrefcount(x)  #读取头部引用计数，形参也会增加一次引用

y = x
print sys.getrefcount(x)

del y
print sys.getrefcount(x)
