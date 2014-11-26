#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jiaojianfeng'

import copy

a = object()

b = a
print a is b


print hex(id(a)), hex(id(b))   # 地址相同，用一个对象

def test(x):
	print hex(id(x))

print test(a)



x = object()
l = [x]
l2 = copy.copy(l)    #浅拷贝，仅复制对象本身， 不会复制其成员

print l2 is l
print l2[0] is x

l3 = copy.deepcopy(l)    #神队复制
print l3 is l
print l3[0] is x

