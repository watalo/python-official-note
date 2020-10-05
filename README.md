# Python 官方文档笔记

——watalo



## 学习资料的出处

### 官方文档：

> https://docs.python.org/zh-cn/3.8/tutorial/index.html

### 项目地址：

> https://github.com/watalo/python-official-note

### 项目内容：

- 每个文件夹是一个章节，严格安装官方文档的顺序来
- 每个文件夹里的`标题.md`文件是官方文档内容
- 每个文件夹里附有官方文档里面的每段代码案例，用`.ipynb` 和`.py`两种格式

------

# Python 教程

Python 是一种易于学习又功能强大的编程语言。它提供了高效的高级数据结构，还能简单有效地面向对象编程。Python 优雅的语法和动态类型，以及解释型语言的本质，使它成为多数平台上写脚本和快速开发应用的理想语言。

Python 解释器及丰富的标准库，提供了适用于各个主要系统平台的源码或机器码，这些可以到 Python 官网 https://www.python.org/ 免费获取，并可自由地分发。许多免费的第三方 Python 模块、程序、工具和它们的文档，也能在这个网站上找到对应内容或链接。

Python 解释器易于扩展，可以使用 C 或 C++（或者其他可以从 C 调用的语言）扩展新的功能和数据类型。Python 也可用作可定制化软件中的扩展程序语言。

这个教程非正式地介绍了 Python 语言和系统的基本概念和功能。最好在阅读的时候准备一个 Python 解释器进行练习。所有的例子都是相互独立的，所以这个教程也可以离线阅读。

有关标准的对象和模块，请参阅 [Python 标准库](https://docs.python.org/zh-cn/3.8/library/index.html#library-index)。[Python语言参考](https://docs.python.org/zh-cn/3.8/reference/index.html#reference-index) 提供了更正式的语言定义。想要编写 C 或者 C++ 扩展可以参考 [扩展和嵌入 Python 解释器](https://docs.python.org/zh-cn/3.8/extending/index.html#extending-index) 和 [Python/C API 参考手册](https://docs.python.org/zh-cn/3.8/c-api/index.html#c-api-index)。另外还有不少书籍深入讲解 Python。

这个教程并没有完整地介绍每一个功能，甚至可能没有涉及全部的常用功能。这个教程只介绍 Python 中最值得注意的功能，也会让你体会到这个语言的风格特色。学习完这个教程，你将可以阅读和编写 Python 模块和程序，也可以开始学习 [Python 标准库](https://docs.python.org/zh-cn/3.8/library/index.html#library-index)。

[术语对照表](https://docs.python.org/zh-cn/3.8/glossary.html#glossary) 也很值得一读。

- [1. 课前甜点](https://docs.python.org/zh-cn/3.8/tutorial/appetite.html)
- 2. 使用 Python 解释器
  
  - 2.1. 调用解释器
    - [2.1.1. 传入参数](https://docs.python.org/zh-cn/3.8/tutorial/interpreter.html#argument-passing)
    - [2.1.2. 交互模式](https://docs.python.org/zh-cn/3.8/tutorial/interpreter.html#interactive-mode)
  - 2.2. 解释器的运行环境
    - [2.2.1. 源文件的字符编码](https://docs.python.org/zh-cn/3.8/tutorial/interpreter.html#source-code-encoding)
- 3. Python 的非正式介绍
  
  - 3.1. Python 作为计算器使用
    - [3.1.1. 数字](https://docs.python.org/zh-cn/3.8/tutorial/introduction.html#numbers)
    - [3.1.2. 字符串](https://docs.python.org/zh-cn/3.8/tutorial/introduction.html#strings)
    - [3.1.3. 列表](https://docs.python.org/zh-cn/3.8/tutorial/introduction.html#lists)
  - [3.2. 走向编程的第一步](https://docs.python.org/zh-cn/3.8/tutorial/introduction.html#first-steps-towards-programming)
- 4. 其他流程控制工具
  
  - [4.1. `if` 语句](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#if-statements)
  - [4.2. `for` 语句](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#for-statements)
  - [4.3. `range()` 函数](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#the-range-function)
  - [4.4. `break` 和 `continue` 语句，以及循环中的 `else` 子句](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
  - [4.5. `pass` 语句](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#pass-statements)
  - [4.6. 定义函数](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#defining-functions)
  - 4.7. 函数定义的更多形式
    - [4.7.1. 参数默认值](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#default-argument-values)
    - [4.7.2. 关键字参数](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#keyword-arguments)
    - 4.7.3. 特殊参数
      - [4.7.3.1. 位置或关键字参数](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#positional-or-keyword-arguments)
      - [4.7.3.2. 仅限位置参数](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#positional-only-parameters)
      - [4.7.3.3. 仅限关键字参数](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#keyword-only-arguments)
      - [4.7.3.4. 函数示例](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#function-examples)
      - [4.7.3.5. 概括](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#recap)
    - [4.7.4. 任意的参数列表](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#arbitrary-argument-lists)
    - [4.7.5. 解包参数列表](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#unpacking-argument-lists)
    - [4.7.6. Lambda 表达式](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#lambda-expressions)
    - [4.7.7. 文档字符串](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#documentation-strings)
    - [4.7.8. 函数标注](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#function-annotations)
  - [4.8. 小插曲：编码风格](https://docs.python.org/zh-cn/3.8/tutorial/controlflow.html#intermezzo-coding-style)
- 5. 数据结构
  
  - 5.1. 列表的更多特性
    - [5.1.1. 列表作为栈使用](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#using-lists-as-stacks)
    - [5.1.2. 列表作为队列使用](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#using-lists-as-queues)
    - [5.1.3. 列表推导式](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#list-comprehensions)
    - [5.1.4. 嵌套的列表推导式](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#nested-list-comprehensions)
  - [5.2. `del` 语句](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#the-del-statement)
  - [5.3. 元组和序列](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#tuples-and-sequences)
  - [5.4. 集合](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#sets)
  - [5.5. 字典](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#dictionaries)
  - [5.6. 循环的技巧](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#looping-techniques)
  - [5.7. 深入条件控制](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#more-on-conditions)
  - [5.8. 比较序列和其他类型](https://docs.python.org/zh-cn/3.8/tutorial/datastructures.html#comparing-sequences-and-other-types)
- 6. 模块
  
  - 6.1. 更多有关模块的信息
    - [6.1.1. 以脚本的方式执行模块](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#executing-modules-as-scripts)
    - [6.1.2. 模块搜索路径](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#the-module-search-path)
    - [6.1.3. “编译过的”Python文件](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#compiled-python-files)
  - [6.2. 标准模块](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#standard-modules)
  - [6.3. `dir()` 函数](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#the-dir-function)
  - 6.4. 包
    - [6.4.1. 从包中导入 *](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#importing-from-a-package)
    - [6.4.2. 子包参考](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#intra-package-references)
    - [6.4.3. 多个目录中的包](https://docs.python.org/zh-cn/3.8/tutorial/modules.html#packages-in-multiple-directories)
- 7. 输入输出
  
  - 7.1. 更漂亮的输出格式
    - [7.1.1. 格式化字符串文字](https://docs.python.org/zh-cn/3.8/tutorial/inputoutput.html#formatted-string-literals)
    - [7.1.2. 字符串的 format() 方法](https://docs.python.org/zh-cn/3.8/tutorial/inputoutput.html#the-string-format-method)
    - [7.1.3. 手动格式化字符串](https://docs.python.org/zh-cn/3.8/tutorial/inputoutput.html#manual-string-formatting)
    - [7.1.4. 旧的字符串格式化方法](https://docs.python.org/zh-cn/3.8/tutorial/inputoutput.html#old-string-formatting)
  - 7.2. 读写文件
    - [7.2.1. 文件对象的方法](https://docs.python.org/zh-cn/3.8/tutorial/inputoutput.html#methods-of-file-objects)
    - [7.2.2. 使用 `json` 保存结构化数据](https://docs.python.org/zh-cn/3.8/tutorial/inputoutput.html#saving-structured-data-with-json)
- 8. 错误和异常
  
  - [8.1. 语法错误](https://docs.python.org/zh-cn/3.8/tutorial/errors.html#syntax-errors)
  - [8.2. 异常](https://docs.python.org/zh-cn/3.8/tutorial/errors.html#exceptions)
  - [8.3. 处理异常](https://docs.python.org/zh-cn/3.8/tutorial/errors.html#handling-exceptions)
  - [8.4. 抛出异常](https://docs.python.org/zh-cn/3.8/tutorial/errors.html#raising-exceptions)
  - [8.5. 用户自定义异常](https://docs.python.org/zh-cn/3.8/tutorial/errors.html#user-defined-exceptions)
  - [8.6. 定义清理操作](https://docs.python.org/zh-cn/3.8/tutorial/errors.html#defining-clean-up-actions)
  - [8.7. 预定义的清理操作](https://docs.python.org/zh-cn/3.8/tutorial/errors.html#predefined-clean-up-actions)
- 9. 类
  
  - [9.1. 名称和对象](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#a-word-about-names-and-objects)
  - 9.2. Python 作用域和命名空间
    - [9.2.1. 作用域和命名空间示例](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#scopes-and-namespaces-example)
  - 9.3. 初探类
    - [9.3.1. 类定义语法](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#class-definition-syntax)
    - [9.3.2. 类对象](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#class-objects)
    - [9.3.3. 实例对象](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#instance-objects)
    - [9.3.4. 方法对象](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#method-objects)
    - [9.3.5. 类和实例变量](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#class-and-instance-variables)
  - [9.4. 补充说明](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#random-remarks)
  - 9.5. 继承
    - [9.5.1. 多重继承](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#multiple-inheritance)
  - [9.6. 私有变量](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#private-variables)
  - [9.7. 杂项说明](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#odds-and-ends)
  - [9.8. 迭代器](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#iterators)
  - [9.9. 生成器](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#generators)
  - [9.10. 生成器表达式](https://docs.python.org/zh-cn/3.8/tutorial/classes.html#generator-expressions)
- 10. 标准库简介
  
  - [10.1. 操作系统接口](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#operating-system-interface)
  - [10.2. 文件通配符](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#file-wildcards)
  - [10.3. 命令行参数](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#command-line-arguments)
  - [10.4. 错误输出重定向和程序终止](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#error-output-redirection-and-program-termination)
  - [10.5. 字符串模式匹配](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#string-pattern-matching)
  - [10.6. 数学](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#mathematics)
  - [10.7. 互联网访问](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#internet-access)
  - [10.8. 日期和时间](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#dates-and-times)
  - [10.9. 数据压缩](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#data-compression)
  - [10.10. 性能测量](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#performance-measurement)
  - [10.11. 质量控制](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#quality-control)
  - [10.12. 自带电池](https://docs.python.org/zh-cn/3.8/tutorial/stdlib.html#batteries-included)
- 11. 标准库简介 —— 第二部分
  
  - [11.1. 格式化输出](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#output-formatting)
  - [11.2. 模板](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#templating)
  - [11.3. 使用二进制数据记录格式](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#working-with-binary-data-record-layouts)
  - [11.4. 多线程](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#multi-threading)
  - [11.5. 日志记录](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#logging)
  - [11.6. 弱引用](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#weak-references)
  - [11.7. 用于操作列表的工具](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#tools-for-working-with-lists)
  - [11.8. 十进制浮点运算](https://docs.python.org/zh-cn/3.8/tutorial/stdlib2.html#decimal-floating-point-arithmetic)
- 12. 虚拟环境和包
  
  - [12.1. 概述](https://docs.python.org/zh-cn/3.8/tutorial/venv.html#introduction)
  - [12.2. 创建虚拟环境](https://docs.python.org/zh-cn/3.8/tutorial/venv.html#creating-virtual-environments)
  - [12.3. 使用pip管理包](https://docs.python.org/zh-cn/3.8/tutorial/venv.html#managing-packages-with-pip)
- [13. 接下来？](https://docs.python.org/zh-cn/3.8/tutorial/whatnow.html)
- 14. 交互式编辑和编辑历史
  
  - [14.1. Tab 补全和编辑历史](https://docs.python.org/zh-cn/3.8/tutorial/interactive.html#tab-completion-and-history-editing)
  - [14.2. 默认交互式解释器的替代品](https://docs.python.org/zh-cn/3.8/tutorial/interactive.html#alternatives-to-the-interactive-interpreter)
- 15. 浮点算术：争议和限制
  
  - [15.1. 表示性错误](https://docs.python.org/zh-cn/3.8/tutorial/floatingpoint.html#representation-error)
- 16. 附录
  
  - 16.1. 交互模式
    - [16.1.1. 错误处理](https://docs.python.org/zh-cn/3.8/tutorial/appendix.html#error-handling)
    - [16.1.2. 可执行的Python脚本](https://docs.python.org/zh-cn/3.8/tutorial/appendix.html#executable-python-scripts)
    - [16.1.3. 交互式启动文件](https://docs.python.org/zh-cn/3.8/tutorial/appendix.html#the-interactive-startup-file)
    - [16.1.4. 定制模块](https://docs.python.org/zh-cn/3.8/tutorial/appendix.html#the-customization-modules)