#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:4.7 函数定义的更多形式.py
@TIME		:2020/10/03 01:41:56
@AUTHOR     :watalo
@VERSION	:0.0.x
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

# 4.7.2 关键字参数

def parrot(voltage, state='a stiff', action = 'voom', type = 'Norwegian Blue'):
    """
    也可以使用形如 kwarg=value 的 关键字参数 来调用函数。
    接受一个必需的参数（voltage）和三个可选的参数（state, action，和 type）
    """
    print("--This paarot wouldn't", action, end='')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage,the", type)
    print("--It's", state, '!')

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# 但下面的函数调用都是无效的:

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


'''
1-关键字参数必须跟随在位置参数的后面。
2-传递的所有关键字参数必须与函数接受的其中一个参数匹配，它们的顺序并不重要。
    这也包括非可选参数，（比如 parrot(voltage=1000) 也是有效的）。
3-不能对同一个参数多次赋值。
'''

def func(a):
    '''
    :description:
    :param {var}:
    :return:
    '''
    pass

# func(0,a=0) # TypeError: func() got multiple values for argument 'a'

'''
当存在一个形式为 **name 的最后一个形参时，它会接收一个字典 (参见 映射类型 --- dict)，其中包含除了与已有形
参相对应的关键字参数以外的所有关键字参数。 这可以与一个形式为 *name，接收一个包含除了已有形参列表以外的位置
参数的 元组 的形参 (将在下一小节介绍) 组合使用 (*name 必须出现在 **name 之前。) 例如，如果我们这样定义一个
函数:
'''

def cheeseshop(kind, *args, **kwargs):
    print('--Do you have any',kind, '?')
    print("--I'm sorry, we're all out of", kind)
    for a in args:
        print(a)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ':',kwargs[kw])

cheeseshop('Limburger', 
            "It's very ruuny, sir.",
            "It's really very, VERY RUUNY,sir.", 
            shopkeeper='Michael Palin', 
            client = 'John cleese', 
            sketch="cheese shop sketch")   
