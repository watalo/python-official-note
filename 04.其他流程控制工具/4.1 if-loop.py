#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:4.1 if-loop.py
@TIME		:2020/10/02 17:51:27
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

x = int(input('Please enter an integer:'))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0 :
    print('ZERO')
elif x == 1:
    print("Single")
else:
    print('More')