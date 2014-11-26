#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jiaojianfeng'

class User(object):
	def __del__(self):
		print "Will be dead"

a = User()
b = a

import sys
print sys.getrefcount(a)

del a
print sys.getrefcount(b)   

del b  # 引用删除，对象被回收