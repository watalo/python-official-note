#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   09.namespaces_scope.py
@Time    :   2021/01/07 00:02:36
@Author  :   watalo 
@Version :   1.0
@Contact :   watalo@163.com
'''

# here put the import lib

import os
from sys import argv

class test:
   pass

def test2(arg1, arg2):
   print(locals())
   return arg1 + arg2

def test3():
   b = 100
   def test4():
      b = 10000
      print(locals())
      return b
   test4()
   print(locals())

a = 1
b = 2
test2(a, b)
test3()
print(globals())

