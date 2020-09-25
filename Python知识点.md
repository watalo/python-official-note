# PYTHON官方文档知识点

## 1、源文件的字符编码

默认情况下，Python 源码文件以 UTF-8 编码方式处理。但可以使用特殊注释使用别的编码。

`# -*- coding:encoding -*-` encoding 表示编码类型。

**编码声明**是这样的：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

## 2、注释

Python中的注释以井号 `#` 开头，并且一直延伸到该文本行结束为止。注释可以出现在一行的开头或者是空白和代码的后边，但是不能出现在字符串中间。字符串中的井号就是井号。

```python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

## 3、转义符

反斜杠 `\` 可以用来转义，几个特殊的转义符组合：



