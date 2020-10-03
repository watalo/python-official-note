#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.7 特殊参数.py
@Time    :   2020/10/04 01:20:35
@Author  :   watalo 
@Version :   1.0
@Contact :   watalo@163.com
'''

# here put the import lib

def fod(var, *args ,**kwargs):
    print('var变量的值是{}'.format(var))
    print('*args变量接收一个元组，接受多个参数，比如{}'.format([*args]))
    print("**kwargs变量接受一个字典，这次接收的参数如下：")
    for a in kwargs:
        print(a,':',kwargs[a])

fod(1, 2,3, a= 9)