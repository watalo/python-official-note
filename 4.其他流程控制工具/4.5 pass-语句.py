
'''
pass 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它。例如:
'''
while True:
    pass

'''
这通常用于创建最小的类:
'''
class MyEmptyClass:
    pass

'''
pass 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，
允许你保持在更抽象的层次上进行思考。 pass 会被静默地忽略:
'''
def initlog(*args):
    pass

    