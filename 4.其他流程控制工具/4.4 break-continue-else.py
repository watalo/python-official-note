#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:4.4 break-continue-else.py
@TIME		:2020/10/02 18:49:14
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

'''
break 语句，和 C 中的类似，用于跳出最近的 for 或 while 循环.

循环语句可能带有 else 子句；
它会在循环耗尽了可迭代对象 (使用 for) 或循环条件变为假值 (使用 while) 时被执行，
但不会在循环被 break 语句终止时被执行。 以下搜索素数的循环就是这样的一个例子:

'''


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n,'=', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


##########################################
'''
（是的，这是正确的代码。仔细看： else 子句属于 for 循环， 不属于 if 语句。）

当和循环一起使用时，else 子句与 try 语句中的 else 子句的共同点多于 if 语句中的同类子句: 
try 语句中的 else 子句会在未发生异常时执行，而循环中的 else 子句则会在未发生 break 时执行。 
有关 try 语句和异常的更多信息，请参阅 处理异常。

continue 语句也是借鉴自 C 语言，表示继续循环中的下一次迭代:
'''

for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('Found an odd number', num)