#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:3.2 第一步.py
@TIME		:2020/10/02 17:28:16
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

'''
斐波拉契数列
'''
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


'''
第一行含有一个 多重赋值: 变量 a 和 b 同时得到了新值 0 和 1. 最后一行又用了一次多重赋值, 这展示出了右手边的表达式，在任何赋值发生之前就被求值了。右手边的表达式是从左到右被求值的。

while 循环只要它的条件（这里指： a < 10）保持为真就会一直执行。Python 和 C 一样，任何非零整数都为真；零为假。这个条件也可以是字符串或是列表的值，事实上任何序列都可以；长度非零就为真，空序列就为假。在这个例子里，判断条件是一个简单的比较。标准的比较操作符的写法和 C 语言里是一样： < （小于）、 > （大于）、 == （等于）、 <= （小于或等于)、 >= （大于或等于）以及 != （不等于）。

循环体 是 缩进的 ：缩进是 Python 组织语句的方式。在交互式命令行里，你得给每个缩进的行敲下 Tab 键或者（多个）空格键。实际上用文本编辑器的话，你要准备更复杂的输入方式；所有像样的文本编辑器都有自动缩进的设置。交互式命令行里，当一个组合的语句输入时, 需要在最后敲一个空白行表示完成（因为语法分析器猜不出来你什么时候打的是最后一行）。注意，在同一块语句中的每一行，都要缩进相同的长度。

print() 函数将所有传进来的参数值打印出来. 它和直接输入你要显示的表达式(比如我们之前在计算器的例子里做的)不一样， print() 能处理多个参数，包括浮点数，字符串。 字符串会打印不带引号的内容, 并且在参数项之间会插入一个空格, 这样你就可以很好的把东西格式化, 像这样:
'''

'''
改进版：
关键字参数end可以用来取消输出后面的换行，或使用领蛙一个字符串来结尾：
'''

while a < 1000:
    print(a, end = ',')
    a, b = b, a+b

    