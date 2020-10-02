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

'''
关键字 def 引入一个函数 定义。它必须后跟函数名称和带括号的形式参数列表。构成函数体的语句从下一行开始，并且
必须缩进。函数体的第一个语句可以（可选的）是字符串文字；这个字符串文字是函数的文档字符串或 docstring。（有
关文档字符串的更多信息，请参阅 文档字符串 部分）有些工具使用文档字符串自动生成在线或印刷文档，或者让用户以
交互式的形式浏览代码；在你编写的代码中包含文档字符串是一种很好的做法，所以要养成习惯。函数的 执行 会引入一个
用于函数局部变量的新符号表。 更确切地说，函数中所有的变量赋值都将存储在局部符号表中；而变量引用会首先在局部
符号表中查找，然后是外层函数的局部符号表，再然后是全局符号表，最后是内置名称的符号表。 因此，全局变量和外层
函数的变量不能在函数内部直接赋值（除非是在 global 语句中定义的全局变量，或者是在 nonlocal 语句中定义的外层
函数的变量），尽管它们可以被引用。在函数被调用时，实际参数（实参）会被引入被调用函数的本地符号表中；因此，实
参是通过 按值调用 传递的（其中 值 始终是对象 引用 而不是对象的值）。当一个函数调用另外一个函数时，将会为该调
用创建一个新的本地符号表。函数定义会将函数名称与函数对象在当前符号表中进行关联。 解释器会将该名称所指向的对象
识别为用户自定义函数。 其他名称也可指向同一个函数对象并可被用来访问访函数:
'''




def ask_ok(prompt, retries=4,reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
            
i = 5

def f(arg = i):
    """
    docstring
    """
    print(arg)
    
def foo(a, L=[]):
    """
    默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。
    比如，下面的函数会存储在后续调用中传递给它的参数:
    """
    L.append(a)
    return L

def fob(a, L=None):
    """
    如果你不想要在后续调用之间共享默认值，你可以这样写这个函数
    """
    if L is None:
        L =[]
    L.append(a)
    return L


if __name__ == "__main__":
    # fib(2000)

    # i = 6 
    # f()


    print(foo(1))
    print(foo(2))
    print(foo(3))
    print(fob(1))
    print(fob(2))
    print(fob(3))