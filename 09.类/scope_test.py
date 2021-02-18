#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:test.py
@TIME		:2021/02/13 23:25:53
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

# 1.局部无变量的时候，向外找全局变量
# def low_scope():
#     print(s)

# s = 1
# low_scope()


# 2.局部名字的作用域就是在局部，不会影响全局变量
# def low_scope():
#     s = 'low scope'

# s = 'upper scope'
# low_scope()
# print(s)

# 3.可变对象，同一个命名空间中的名字对应的对象可以在局部作用域里更改元素
# def low_scope():
#     l[0] = 2

# l = [1, 2]
# low_scope()
# print(l)

# 4.可变对象，直接执行对名字的操作，而不是对象的元素时，是直接作用于名字

def low_scope():
    l = [1, 2] #  --> low_scope.l

l = [2, 2] # --> l
low_scope()
print(l)