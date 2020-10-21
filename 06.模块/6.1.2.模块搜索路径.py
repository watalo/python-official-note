#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:6.1.2.模块搜索路径.py
@TIME		:2020/10/12 00:19:37
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

'''
sys.path 初始有这些目录地址:

    包含输入脚本的目录（或者未指定文件时的当前目录）。
    PYTHONPATH （一个包含目录名称的列表，它和shell变量 PATH 有一样的语法）。
    取决于安装的默认设置
'''



import sys
import test

for path in sys.path:
    print(path)

