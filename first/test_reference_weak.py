#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jiaojianfeng'

import sys, weakref

class User(object): pass

def callback(r):
	print "weakref object:", r
	print "target object dead!"

a = User()

r = weakref.ref(a, callback)

print sys.getrefcount(a)

print r() is a

del a

print hex(id(r))

print r() is None