'''
Author: your name
Date: 2020-10-02 18:58:27
LastEditTime: 2020-10-02 19:03:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python教程官方文档\4.其他流程控制工具\4.6 定义函数.py
'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:4.6 定义函数.py
@TIME		:2020/10/02 18:58:34
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

'''
我们可以创建一个输出任意范围内 Fibonacci 数列的函数:
'''


def fib(n):


    a,b =0,1
    while a < n:
        print(a,end=' ')
        a,b = b, a + b
    print()



if __name__ == "__main__":
    fib(2000)