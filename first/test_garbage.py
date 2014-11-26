#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jiaojianfeng'

# Python 使用的是引用计数，循环依赖的解决靠的是专门处理循环引用的GC
# Java 就避开了这点，使用的是标记清除，从root出发

#各有千秋

import gc

class User(object):
	"""docstring for User"""
	def __del__(self):
		print hex(id(self)), "will be dead!"

gc.disable()  # 禁用gc，  在无循环依赖时 可以显著提升性能

a = User()
del a


print gc.get_count()  #各级代龄链表跟踪的对象数量

print gc.get_threshold()  #获取各级代龄阈值