############################
# import sound.effects.echo

# echofilter() # name 'echofilter' is not defined

# sound.effects.echo.echofilter() # 执行成功

#########################################
# from sound.effects import echo

# echo.echofilter() # 执行成功

#########################################
# from sound.effects.echo import echofilter

# echofilter() # 执行成功
 

import sound.effects.echo
import sound.effects.surround # 注意看 ./effects/surround.py 里的注释
from sound.effects import *


list_echo = dir(sound.effects.echo)
print(list_echo)
list_surround = dir(sound.effects.surround)
print(list_surround)
list_reverse = dir(sound.effects.reverse)
print(list_reverse)


'''
6.4.3. 多个目录中的包
包支持另一个特殊属性， __path__ 。
它被初始化为一个列表，其中包含在执行该文件中的代码之前保存包的文件 __init__.py 的目录的名称。
这个变量可以修改；这样做会影响将来对包中包含的模块和子包的搜索。
虽然通常不需要此功能，但它可用于扩展程序包中的模块集。

https://docs.python.org/zh-cn/3.9/reference/import.html#__path__
'''
