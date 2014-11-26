#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jiaojianfeng'

import sys

import test_sys

x = 123

print globals()

globals()["y"] = "hello world"

print y

print type(y)

y = __import__("string")

print type(y)

print y.digits

print globals() is locals()   # 在函数外部，这两者一样

print locals()


def test(x):
	y = x + 100
	print locals()
	print globals() is locals()

	frame = sys._getframe(0)  # 获取当前堆栈帧

	print locals() is frame.f_locals
	print globals() is frame.f_globals

print test(123)

print test_sys.__dict__
