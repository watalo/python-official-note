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

a = 1
b = [1]




def Func():
   
   a = 11
   b = 222
   print(locals())

class Main():
   def __init__():
       pass

# if __name__ == '__main__':
Func()
print(globals())