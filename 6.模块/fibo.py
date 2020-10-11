# fibonacii numbers module


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


'''
以脚本来运行的时候，这个脚本文件的__name__叫做"__main__",
以模块被导入时，脚本文件的—__name__不是"__main__",
所以 if 这句话下面的代码不会执行。
'''
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))