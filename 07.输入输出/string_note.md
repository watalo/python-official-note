# [`string`](https://docs.python.org/zh-cn/3/library/string.html#module-string) --- 常见的字符串操作[¶](https://docs.python.org/zh-cn/3/library/string.html#module-string)

**源代码：** [Lib/string.py](https://github.com/python/cpython/tree/3.9/Lib/string.py)

------

参见

[文本序列类型 --- str](https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq)

[字符串的方法](https://docs.python.org/zh-cn/3/library/stdtypes.html#string-methods)

## 字符串常量

此模块中定义的常量为：

- `string.``ascii_letters`

  下文所述 [`ascii_lowercase`](https://docs.python.org/zh-cn/3/library/string.html#string.ascii_lowercase) 和 [`ascii_uppercase`](https://docs.python.org/zh-cn/3/library/string.html#string.ascii_uppercase) 常量的拼连。 该值不依赖于语言区域。

- `string.``ascii_lowercase`

  小写字母 `'abcdefghijklmnopqrstuvwxyz'`。 该值不依赖于语言区域，不会发生改变。

- `string.``ascii_uppercase`

  大写字母 `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`。 该值不依赖于语言区域，不会发生改变。

- `string.``digits`

  字符串 `'0123456789'`。

- `string.``hexdigits`

  字符串 `'0123456789abcdefABCDEF'`。

- `string.``octdigits`

  字符串 `'01234567'`。

- `string.``punctuation`

  由在 `C` 区域设置中被视为标点符号的 ASCII 字符所组成的字符串: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`.

- `string.``printable`

  由被视为可打印符号的 ASCII 字符组成的字符串。 这是 [`digits`](https://docs.python.org/zh-cn/3/library/string.html#string.digits), [`ascii_letters`](https://docs.python.org/zh-cn/3/library/string.html#string.ascii_letters), [`punctuation`](https://docs.python.org/zh-cn/3/library/string.html#string.punctuation) 和 [`whitespace`](https://docs.python.org/zh-cn/3/library/string.html#string.whitespace) 的总和。

- `string.``whitespace`

  由被视为空白符号的 ASCII 字符组成的字符串。 其中包括空格、制表、换行、回车、进纸和纵向制表符。



## 自定义字符串格式化

内置的字符串类提供了通过使用 [**PEP 3101**](https://www.python.org/dev/peps/pep-3101) 所描述的 [`format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法进行复杂变量替换和值格式化的能力。 [`string`](https://docs.python.org/zh-cn/3/library/string.html#module-string) 模块中的 [`Formatter`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter) 类允许你使用与内置 [`format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法相同的实现来创建并定制你自己的字符串格式化行为。

- *class* `string.``Formatter`

  [`Formatter`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter) 类包含下列公有方法：`format`(*format_string*, */*, **args*, ***kwargs*)首要的 API 方法。 它接受一个格式字符串和任意一组位置和关键字参数。 它只是一个调用 [`vformat()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.vformat) 的包装器。*在 3.7 版更改:* 格式字符串参数现在是 [仅限位置参数](https://docs.python.org/zh-cn/3/glossary.html#positional-only-parameter)。`vformat`(*format_string*, *args*, *kwargs*)此函数执行实际的格式化操作。 它被公开为一个单独的函数，用于需要传入一个预定义字母作为参数，而不是使用 `*args` 和 `**kwargs` 语法将字典解包为多个单独参数并重打包的情况。 [`vformat()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.vformat) 完成将格式字符串分解为字符数据和替换字段的工作。 它会调用下文所述的几种不同方法。此外，[`Formatter`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter) 还定义了一些旨在被子类替换的方法：`parse`(*format_string*)循环遍历 format_string 并返回一个由可迭代对象组成的元组 (*literal_text*, *field_name*, *format_spec*, *conversion*)。 它会被 [`vformat()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.vformat) 用来将字符串分解为文本字面值或替换字段。元组中的值在概念上表示一段字面文本加上一个替换字段。 如果没有字面文本（如果连续出现两个替换字段就会发生这种情况），则 *literal_text* 将是一个长度为零的字符串。 如果没有替换字段，则 *field_name*, *format_spec* 和 *conversion* 的值将为 `None`。`get_field`(*field_name*, *args*, *kwargs*)给定 *field_name* 作为 [`parse()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.parse) (见上文) 的返回值，将其转换为要格式化的对象。 返回一个元组 (obj, used_key)。 默认版本接受在 [**PEP 3101**](https://www.python.org/dev/peps/pep-3101) 所定义形式的字符串，例如 "0[name]" 或 "label.title"。 *args* 和 *kwargs* 与传给 [`vformat()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.vformat) 的一样。 返回值 *used_key* 与 [`get_value()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.get_value) 的 *key* 形参具有相同的含义。`get_value`(*key*, *args*, *kwargs*)提取给定的字段值。 *key* 参数将为整数或字符串。 如果是整数，它表示 *args* 中位置参数的索引；如果是字符串，它表示 *kwargs* 中的关键字参数名。*args* 形参会被设为 [`vformat()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.vformat) 的位置参数列表，而 *kwargs* 形参会被设为由关键字参数组成的字典。对于复合字段名称，仅会为字段名称的第一个组件调用这些函数；后续组件会通过普通属性和索引操作来进行处理。因此举例来说，字段表达式 '0.name' 将导致调用 [`get_value()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.get_value) 时附带 *key* 参数值 0。 在 [`get_value()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.get_value) 通过调用内置的 [`getattr()`](https://docs.python.org/zh-cn/3/library/functions.html#getattr) 函数返回后将会查找 `name` 属性。如果索引或关键字引用了一个不存在的项，则将引发 [`IndexError`](https://docs.python.org/zh-cn/3/library/exceptions.html#IndexError) 或 [`KeyError`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyError)。`check_unused_args`(*used_args*, *args*, *kwargs*)在必要时实现对未使用参数进行检测。 此函数的参数是是格式字符串中实际引用的所有参数键的集合（整数表示位置参数，字符串表示名称参数），以及被传给 vformat 的 *args* 和 *kwargs* 的引用。 未使用参数的集合可以根据这些形参计算出来。 如果检测失败则 [`check_unused_args()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.check_unused_args) 应会引发一个异常。`format_field`(*value*, *format_spec*)[`format_field()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.format_field) 会简单地调用内置全局函数 [`format()`](https://docs.python.org/zh-cn/3/library/functions.html#format)。 提供该方法是为了让子类能够重载它。`convert_field`(*value*, *conversion*)使用给定的转换类型（来自 [`parse()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.parse) 方法所返回的元组）来转换（由 [`get_field()`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter.get_field) 所返回的）值。 默认版本支持 's' (str), 'r' (repr) 和 'a' (ascii) 等转换类型。



## 格式字符串语法

[`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法和 [`Formatter`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter) 类共享相同的格式字符串语法（虽然对于 [`Formatter`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter) 来说，其子类可以定义它们自己的格式字符串语法）。 具体语法与 [格式化字符串字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#f-strings) 相似，但也存在区别。

格式字符串包含有以花括号 `{}` 括起来的“替换字段”。 不在花括号之内的内容被视为字面文本，会不加修改地复制到输出中。 如果你需要在字面文本中包含花括号字符，可以通过重复来转义: `{{` and `}}`。

替换字段的语法如下：

> ```python
> replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
> field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
> arg_name          ::=  [identifier | digit+]
> attribute_name    ::=  identifier
> element_index     ::=  digit+ | index_string
> index_string      ::=  <any source character except "]"> +
> conversion        ::=  "r" | "s" | "a"
> format_spec       ::=  <described in the next section>
> ```

用不太正式的术语来描述，替换字段开头可以用一个 *field_name* 指定要对值进行格式化并取代替换字符被插入到输出结果的对象。 *field_name* 之后有可选的 *conversion* 字段，它是一个感叹号 `'!'` 加一个 *format_spec*，并以一个冒号 `':'` 打头。 这些指明了替换值的非默认格式。

另请参阅 [格式规格迷你语言](https://docs.python.org/zh-cn/3/library/string.html#formatspec) 一节。

*field_name* 本身以一个数字或关键字 *arg_name* 打头。 如果为数字，则它指向一个位置参数，而如果为关键字，则它指向一个命名关键字参数。 如果格式字符串中的数字 arg_names 为 0, 1, 2, ... 的序列，它们可以全部省略（而非部分省略），数字 0, 1, 2, ... 将会按顺序自动插入。 由于 *arg_name* 不使用引号分隔，因此无法在格式字符串中指定任意的字典键 (例如字符串 `'10'` 或 `':-]'`)。 *arg_name* 之后可以带上任意数量的索引或属性表达式。 `'.name'` 形式的表达式会使用 [`getattr()`](https://docs.python.org/zh-cn/3/library/functions.html#getattr) 选择命名属性，而 `'[index]'` 形式的表达式会使用 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 执行索引查找。

*在 3.1 版更改:* 位置参数说明符对于 [`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 可以省略，因此 `'{} {}'.format(a, b)` 等价于 `'{0} {1}'.format(a, b)`。

*在 3.4 版更改:* 位置参数说明符对于 [`Formatter`](https://docs.python.org/zh-cn/3/library/string.html#string.Formatter) 可以省略。

一些简单的格式字符串示例

```python
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.
```

使用 *conversion* 字段在格式化之前进行类型强制转换。 通常，格式化值的工作由值本身的 [`__format__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__format__) 方法来完成。 但是，在某些情况下最好强制将类型格式化为一个字符串，覆盖其本身的格式化定义。 通过在调用 [`__format__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__format__) 之前将值转换为字符串，可以绕过正常的格式化逻辑。

目前支持的转换旗标有三种: `'!s'` 会对值调用 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str)，`'!r'` 调用 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 而 `'!a'` 则调用 [`ascii()`](https://docs.python.org/zh-cn/3/library/functions.html#ascii)。

几个例子：

```python
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first
```

*format_spec* 字段包含值应如何呈现的规格描述，例如字段宽度、对齐、填充、小数精度等细节信息。 每种值类型可以定义自己的“格式化迷你语言”或对 *format_spec* 的解读方式。

大多数内置类型都支持同样的格式化迷你语言，具体描述见下一节。

*format_spec* 字段还可以在其内部包含嵌套的替换字段。 这些嵌套的替换字段可能包括字段名称、转换旗标和格式规格描述，但是不再允许更深层的嵌套。 format_spec 内部的替换字段会在解读 *format_spec* 字符串之前先被解读。 这将允许动态地指定特定值的格式。

请参阅 [格式示例](https://docs.python.org/zh-cn/3/library/string.html#formatexamples) 一节查看相关示例。



### 格式规格迷你语言

“格式规格”在格式字符串所包含的替换字段内部使用，用于定义单个值应如何呈现 (参见 [格式字符串语法](https://docs.python.org/zh-cn/3/library/string.html#formatstrings) 和 [格式化字符串字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#f-strings))。 它们也可以被直接传给内置的 [`format()`](https://docs.python.org/zh-cn/3/library/functions.html#format) 函数。 每种可格式化的类型都可以自行定义如何对格式规格进行解读。

大多数内置类型都为格式规格实现了下列选项，不过某些格式化选项只被数值类型所支持。

一般约定空的格式描述将产生与在值上调用 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 相同的结果。 非空格式描述通常会修改此结果。

*标准格式说明符* 的一般形式如下：

```python
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

如果指定了一个有效的 *align* 值，则可以在该值前面加一个 *fill* 字符，它可以为任意字符，如果省略则默认为空格符。 在 [格式化字符串字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#f-strings) 或在使用 [`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法时是无法使用花括号字面值 ("`{`" or "`}`") 作为 *fill* 字符的。 但是，通过嵌套替换字段插入花括号则是可以的。 这个限制不会影响 [`format()`](https://docs.python.org/zh-cn/3/library/functions.html#format) 函数。

各种对齐选项的含义如下：

> | 选项  | 意义                                                         |
> | :---- | :----------------------------------------------------------- |
> | `'<'` | 强制字段在可用空间内左对齐（这是大多数对象的默认值）。       |
> | `'>'` | 强制字段在可用空间内右对齐（这是数字的默认值）。             |
> | `'='` | 强制将填充放置在符号（如果有）之后但在数字之前。这用于以“+000000120”形式打印字段。此对齐选项仅对数字类型有效。当'0'紧接在字段宽度之前时，它成为默认值。 |
> | `'^'` | 强制字段在可用空间内居中。                                   |

请注意，除非定义了最小字段宽度，否则字段宽度将始终与填充它的数据大小相同，因此在这种情况下，对齐选项没有意义。

*sign* 选项仅对数字类型有效，可以是以下之一：

> | 选项  | 意义                                           |
> | :---- | :--------------------------------------------- |
> | `'+'` | 表示标志应该用于正数和负数。                   |
> | `'-'` | 表示标志应仅用于负数（这是默认行为）。         |
> | space | 表示应在正数上使用前导空格，在负数上使用减号。 |

`'#'` 选项可以让“替代形式”被用于转换。 替代形式可针对不同类型分别定义。 此选项仅对整数、浮点、复数和 Decimal 类型有效。 对于整数类型，当使用二进制、八进制或十六进制输出时，此选项会为输出值添加相应的 `'0b'`, `'0o'` 或 `'0x'` 前缀。 对于浮点数、复数和 Decimal 类型，替代形式会使得转换结果总是包含小数点符号，即使其不带小数。 通常只有在带有小数的情况下，此类转换的结果中才会出现小数点符号。 此外，对于 `'g'` 和 `'G'` 转换，末尾的零不会从结果中被移除。

`','` 选项表示使用逗号作为千位分隔符。 对于感应区域设置的分隔符，请改用 `'n'` 整数表示类型。

*在 3.1 版更改:* 添加了 `','` 选项 (另请参阅 [**PEP 378**](https://www.python.org/dev/peps/pep-0378))。

`'_'` 选项表示对浮点表示类型和整数表示类型 `'d'` 使用下划线作为千位分隔符。 对于整数表示类型 `'b'`, `'o'`, `'x'` 和 `'X'`，将为每 4 个数位插入一个下划线。 对于其他表示类型指定此选项则将导致错误。

*在 3.6 版更改:* 添加了 `'_'` 选项 (另请参阅 [**PEP 515**](https://www.python.org/dev/peps/pep-0515))。

*width* 是一个定义最小总字段宽度的十进制整数，包括任何前缀、分隔符和其他格式化字符。 如果未指定，则字段宽度将由内容确定。

当未显式给出对齐方式时，在 *width* 字段前加一个零 (`'0'`) 字段将为数字类型启用感知正负号的零填充。 这相当于设置 *fill* 字符为 `'0'` 且 *alignment* 类型为 `'='`。

*precision* 是一个十进制数字，表示对于以 `'f'` and `'F'` 格式化的浮点数值要在小数点后显示多少个数位，或者对于以 `'g'` 或 `'G'` 格式化的浮点数值要在小数点前后共显示多少个数位。 对于非数字类型，该字段表示最大字段大小 —— 换句话说就是要使用多少个来自字段内容的字符。 对于整数值则不允许使用 *precision*。

最后，*type* 确定了数据应如何呈现。

可用的字符串表示类型是：

> | 类型  | 意义                                         |
> | :---- | :------------------------------------------- |
> | `'s'` | 字符串格式。这是字符串的默认类型，可以省略。 |
> | None  | 和 `'s'` 一样。                              |

可用的整数表示类型是：

> | 类型  | 意义                                                         |
> | :---- | :----------------------------------------------------------- |
> | `'b'` | 二进制格式。 输出以 2 为基数的数字。                         |
> | `'c'` | 字符。在打印之前将整数转换为相应的unicode字符。              |
> | `'d'` | 十进制整数。 输出以 10 为基数的数字。                        |
> | `'o'` | 八进制格式。 输出以 8 为基数的数字。                         |
> | `'x'` | 十六进制格式。 输出以 16 为基数的数字，使用小写字母表示 9 以上的数码。 |
> | `'X'` | 十六进制格式。 输出以 16 为基数的数字，使用大写字母表示 9 以上的数码。 |
> | `'n'` | 数字。 这与 `'d'` 相似，不同之处在于它会使用当前区域设置来插入适当的数字分隔字符。 |
> | None  | 和 `'d'` 相同。                                              |

在上述的表示类型之外，整数还可以通过下列的浮点表示类型来格式化 (除了 `'n'` 和 `None`)。 当这样做时，会在格式化之前使用 [`float()`](https://docs.python.org/zh-cn/3/library/functions.html#float) 将整数转换为浮点数。

浮点数和小数值可用的表示类型有：

> | 类型  | 意义                                                         |
> | :---- | :----------------------------------------------------------- |
> | `'e'` | 指数表示。 以使用字母 'e' 来标示指数的科学计数法打印数字。 默认的精度为 `6`。 |
> | `'E'` | 指数表示。 与 `'e'` 相似，不同之处在于它使用大写字母 'E' 作为分隔字符。 |
> | `'f'` | 定点表示。 将数字显示为一个定点数。 默认的精确度为 `6`。     |
> | `'F'` | 定点表示。 与 `'f'` 相似，但会将 `nan` 转为 `NAN` 并将 `inf` 转为 `INF`。 |
> | `'g'` | 常规格式。 对于给定的精度 `p >= 1`，这会将数值舍入到 `p` 位有效数字，再将结果以定点格式或科学计数法进行格式化，具体取决于其值的大小。准确的规则如下：假设使用表示类型 `'e'` 和精度 `p-1` 进行格式化的结果具有指数值 `exp`。 那么如果 `m <= exp < p`，其中 `m` 以 -4 表示浮点值而以 -6 表示 [`Decimal`](https://docs.python.org/zh-cn/3/library/decimal.html#decimal.Decimal) 值，该数字将使用类型 `'f'` 和精度 `p-1-exp` 进行格式化。 否则的话，该数字将使用表示类型 `'e'` 和精度 `p-1` 进行格式化。 在两种情况下，都会从有效数字中移除无意义的末尾零，如果小数点之后没有余下数字则小数点也会被移除，除非使用了 `'#'` 选项。正负无穷，正负零和 nan 会分别被格式化为 `inf`, `-inf`, `0`, `-0` 和 `nan`，无论精度如何设定。精度 `0` 会被视为等同于精度 `1`。 默认精度为 `6`。 |
> | `'G'` | 常规格式。 类似于 `'g'`，不同之处在于当数值非常大时会切换为 `'E'`。 无穷与 NaN 也会表示为大写形式。 |
> | `'n'` | 数字。 这与 `'g'` 相似，不同之处在于它会使用当前区域设置来插入适当的数字分隔字符。 |
> | `'%'` | 百分比。 将数字乘以 100 并显示为定点 (`'f'`) 格式，后面带一个百分号。 |
> | None  | 类似于 `'g'`，不同之处在于当使用定点表示法时，小数点后将至少显示一位。 默认精度与表示给定值所需的精度一样。 整体效果为与其他格式修饰符所调整的 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 输出保持一致。 |



### 格式示例

本节包含 [`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 语法的示例以及与旧式 `%` 格式化的比较。

该语法在大多数情况下与旧式的 `%` 格式化类似，只是增加了 `{}` 和 `:` 来取代 `%`。 例如，，`'%03.2f'` 可以被改写为 `'{:03.2f}'`。

新的格式语法还支持新增的不同选项，将在以下示例中说明。

按位置访问参数:

\>>>

```python
>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
>>> '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
'a, b, c'
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'
>>> '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
'c, b, a'
>>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
'abracadabra'
```

按名称访问参数:

\>>>

```python
>>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
>>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
>>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
'Coordinates: 37.24N, -115.81W'
```

访问参数的属性:

\>>>

```python
>>> c = 3-5j
>>> ('The complex number {0} is formed from the real part {0.real} '
...  'and the imaginary part {0.imag}.').format(c)
'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
>>> class Point:
...     def __init__(self, x, y):
...         self.x, self.y = x, y
...     def __str__(self):
...         return 'Point({self.x}, {self.y})'.format(self=self)
...
>>> str(Point(4, 2))
'Point(4, 2)'
```

访问参数的项:

\>>>

```python
>>> coord = (3, 5)
>>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'
```

替代 `%s` 和 `%r`:

\>>>

```python
>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"
```

对齐文本以及指定宽度:

\>>>

```python
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'
```

替代 `%+f`, `%-f` 和 `% f` 以及指定正负号:

\>>>

```python
>>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
'+3.140000; -3.140000'
>>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
' 3.140000; -3.140000'
>>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
'3.140000; -3.140000'
```

替代 `%x` 和 `%o` 以及转换基于不同进位制的值:

\>>>

```python
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
```

使用逗号作为千位分隔符:

\>>>

```python
>>> '{:,}'.format(1234567890)
'1,234,567,890'
```

表示为百分数:

\>>>

```python
>>> points = 19
>>> total = 22
>>> 'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'
```

使用特定类型的专属格式化:

\>>>

```python
>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'
```

嵌套参数以及更复杂的示例:

\>>>

```python
>>> for align, text in zip('<^>', ['left', 'center', 'right']):
...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
...
'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
>>>
>>> octets = [192, 168, 0, 1]
>>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
>>> int(_, 16)
3232235521
>>>
>>> width = 5
>>> for num in range(5,12): 
...     for base in 'dXob':
...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
...     print()
...
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011
```



## 模板字符串

模板字符串提供了由 [**PEP 292**](https://www.python.org/dev/peps/pep-0292) 所描述的更简便的字符串替换方式。 模板字符串的一个主要用例是文本国际化 (i18n)，因为在此场景下，更简单的语法和功能使得文本翻译过程比使用 Python 的其他内置字符串格式化工具更为方便。 作为基于模板字符串构建以实现 i18n 的库的一个示例，请参看 [flufl.i18n](http://flufli18n.readthedocs.io/en/latest/) 包。

模板字符串支持基于 `$` 的替换，使用以下规则：

- `$$` 为转义符号；它会被替换为单个的 `$`。
- `$identifier` 为替换占位符，它会匹配一个名为 `"identifier"` 的映射键。 在默认情况下，`"identifier"` 限制为任意 ASCII 字母数字（包括下划线）组成的字符串，不区分大小写，以下划线或 ASCII 字母开头。 在 `$` 字符之后的第一个非标识符字符将表明占位符的终结。
- `${identifier}` 等价于 `$identifier`。 当占位符之后紧跟着有效的但又不是占位符一部分的标识符字符时需要使用，例如 `"${noun}ification"`。

在字符串的其他位置出现 `$` 将导致引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。

[`string`](https://docs.python.org/zh-cn/3/library/string.html#module-string) 模块提供了实现这些规则的 [`Template`](https://docs.python.org/zh-cn/3/library/string.html#string.Template) 类。 [`Template`](https://docs.python.org/zh-cn/3/library/string.html#string.Template) 有下列方法：

- *class* `string.``Template`(*template*)

  该构造器接受一个参数作为模板字符串。`substitute`(*mapping={}*, */*, ***kwds*)执行模板替换，返回一个新字符串。 *mapping* 为任意字典类对象，其中的键将匹配模板中的占位符。 或者你也可以提供一组关键字参数，其中的关键字即对应占位符。 当同时给出 *mapping* 和 *kwds* 并且存在重复时，则以 *kwds* 中的占位符为优先。`safe_substitute`(*mapping={}*, */*, ***kwds*)类似于 [`substitute()`](https://docs.python.org/zh-cn/3/library/string.html#string.Template.substitute)，不同之处是如果有占位符未在 *mapping* 和 *kwds* 中找到，不是引发 [`KeyError`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyError) 异常，而是将原始占位符不加修改地显示在结果字符串中。 另一个与 [`substitute()`](https://docs.python.org/zh-cn/3/library/string.html#string.Template.substitute) 的差异是任何在其他情况下出现的 `$` 将简单地返回 `$` 而不是引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。此方法被认为“安全”，因为虽然仍有可能发生其他异常，但它总是尝试返回可用的字符串而不是引发一个异常。 从另一方面来说，[`safe_substitute()`](https://docs.python.org/zh-cn/3/library/string.html#string.Template.safe_substitute) 也可能根本算不上安全，因为它将静默地忽略错误格式的模板，例如包含多余的分隔符、不成对的花括号或不是合法 Python 标识符的占位符等等。[`Template`](https://docs.python.org/zh-cn/3/library/string.html#string.Template) 的实例还提供一个公有数据属性：`template`这是作为构造器的 *template* 参数被传入的对象。 一般来说，你不应该修改它，但并不强制要求只读访问。

以下是一个如何使用模版的示例：

\>>>

```python
>>> from string import Template
>>> s = Template('$who likes $what')
>>> s.substitute(who='tim', what='kung pao')
'tim likes kung pao'
>>> d = dict(who='tim')
>>> Template('Give $who $100').substitute(d)
Traceback (most recent call last):
...
ValueError: Invalid placeholder in string: line 1, col 11
>>> Template('$who likes $what').substitute(d)
Traceback (most recent call last):
...
KeyError: 'what'
>>> Template('$who likes $what').safe_substitute(d)
'tim likes $what'
```

进阶用法：你可以派生 [`Template`](https://docs.python.org/zh-cn/3/library/string.html#string.Template) 的子类来自定义占位符语法、分隔符，或用于解析模板字符串的整个正则表达式。 为此目的，你可以重载这些类属性：

- *delimiter* -- 这是用来表示占位符的起始的分隔符的字符串字面值。 默认值为 `$`。 请注意此参数 *不能* 为正则表达式，因为其实现将在必要时对此字符串调用 [`re.escape()`](https://docs.python.org/zh-cn/3/library/re.html#re.escape)。 还要注意你不能在创建类之后改变此分隔符（例如在子类的类命名空间中必须设置不同的分隔符）。

- *idpattern* -- 这是用来描述不带花括号的占位符的模式的正则表达式。 默认值为正则表达式 `(?a:[_a-z][_a-z0-9]*)`。 如果给出了此属性并且 *braceidpattern* 为 `None` 则此模式也将作用于带花括号的占位符。

  注解

   

  由于默认的 *flags* 为 `re.IGNORECASE`，模式 `[a-z]` 可以匹配某些非 ASCII 字符。 因此我们在这里使用了局部旗标 `a`。

  *在 3.7 版更改:* *braceidpattern* 可被用来定义对花括号内部和外部进行区分的模式。

- *braceidpattern* -- 此属性类似于 *idpattern* 但是用来描述带花括号的占位符的模式。 默认值 `None` 意味着回退到 *idpattern* (即在花括号内部和外部使用相同的模式)。 如果给出此属性，这将允许你为带花括号和不带花括号的占位符定义不同的模式。

  *3.7 新版功能.*

- *flags* -- 将在编译用于识别替换内容的正则表达式被应用的正则表达式旗标。 默认值为 `re.IGNORECASE`。 请注意 `re.VERBOSE` 总是会被加为旗标，因此自定义的 *idpattern* 必须遵循详细正则表达式的约定。

  *3.2 新版功能.*

作为另一种选项，你可以通过重载类属性 *pattern* 来提供整个正则表达式模式。 如果你这样做，该值必须为一个具有四个命名捕获组的正则表达式对象。 这些捕获组对应于上面已经给出的规则，以及无效占位符的规则：

- *escaped* -- 这个组匹配转义序列，在默认模式中即 `$$`。
- *named* -- 这个组匹配不带花括号的占位符名称；它不应当包含捕获组中的分隔符。
- *braced* -- 这个组匹配带有花括号的占位符名称；它不应当包含捕获组中的分隔符或者花括号。
- *invalid* -- 这个组匹配任何其他分隔符模式（通常为单个分隔符），并且它应当出现在正则表达式的末尾。

## 辅助函数

- `string.``capwords`(*s*, *sep=None*)

  使用 [`str.split()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.split) 将参数拆分为单词，使用 [`str.capitalize()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.capitalize) 将单词转为大写形式，使用 [`str.join()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.join) 将大写的单词进行拼接。 如果可选的第二个参数 *sep* 被省略或为 `None`，则连续的空白字符会被替换为单个空格符并且开头和末尾的空白字符会被移除，否则 *sep* 会被用来拆分和拼接单词。



## `printf` 风格的字符串格式化

注解

 

此处介绍的格式化操作具有多种怪异特性，可能导致许多常见错误（例如无法正确显示元组和字典）。 使用较新的 [格式化字符串字面值](https://docs.python.org/zh-cn/3.9/reference/lexical_analysis.html#f-strings)，[`str.format()`](https://docs.python.org/zh-cn/3.9/library/stdtypes.html#str.format) 接口或 [模板字符串](https://docs.python.org/zh-cn/3.9/library/string.html#template-strings) 有助于避免这样的错误。 这些替代方案中的每一种都更好地权衡并提供了简单、灵活以及可扩展性优势。

字符串具有一种特殊的内置操作：使用 `%` (取模) 运算符。 这也被称为字符串的 *格式化* 或 *插值* 运算符。 对于 `format % values` (其中 *format* 为一个字符串)，在 *format* 中的 `%` 转换标记符将被替换为零个或多个 *values* 条目。 其效果类似于在 C 语言中使用 `sprintf()`。

如果 *format* 要求一个单独参数，则 *values* 可以为一个非元组对象。 [5](https://docs.python.org/zh-cn/3.9/library/stdtypes.html#id16) 否则的话，*values* 必须或者是一个包含项数与格式字符串中指定的转换符项数相同的元组，或者是一个单独映射对象（例如字典）。

转换标记符包含两个或更多字符并具有以下组成，且必须遵循此处规定的顺序：

1. `'%'` 字符，用于标记转换符的起始。
2. 映射键（可选），由加圆括号的字符序列组成 (例如 `(somename)`)。
3. 转换旗标（可选），用于影响某些转换类型的结果。
4. 最小字段宽度（可选）。 如果指定为 `'*'` (星号)，则实际宽度会从 *values* 元组的下一元素中读取，要转换的对象则为最小字段宽度和可选的精度之后的元素。
5. 精度（可选），以在 `'.'` (点号) 之后加精度值的形式给出。 如果指定为 `'*'` (星号)，则实际精度会从 *values* 元组的下一元素中读取，要转换的对象则为精度之后的元素。
6. 长度修饰符（可选）。
7. 转换类型。

当右边的参数为一个字典（或其他映射类型）时，字符串中的格式 *必须* 包含加圆括号的映射键，对应 `'%'` 字符之后字典中的每一项。 映射键将从映射中选取要格式化的值。 例如：

\>>>

```python
>>> print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.
```

在此情况下格式中不能出现 `*` 标记符（因其需要一个序列类的参数列表）。

转换旗标为：

| 标志  | 含义                                                         |
| :---- | :----------------------------------------------------------- |
| `'#'` | 值的转换将使用“替代形式”（具体定义见下文）。                 |
| `'0'` | 转换将为数字值填充零字符。                                   |
| `'-'` | 转换值将靠左对齐（如果同时给出 `'0'` 转换，则会覆盖后者）。  |
| `' '` | (空格) 符号位转换产生的正数（或空字符串）前将留出一个空格。  |
| `'+'` | 符号字符 (`'+'` 或 `'-'`) 将显示于转换结果的开头（会覆盖 "空格" 旗标）。 |

可以给出长度修饰符 (`h`, `l` 或 `L`)，但会被忽略，因为对 Python 来说没有必要 -- 所以 `%ld` 等价于 `%d`。

转换类型为：

| 转换符 | 含义                                                         | 注释 |
| :----- | :----------------------------------------------------------- | :--- |
| `'d'`  | 有符号十进制整数。                                           |      |
| `'i'`  | 有符号十进制整数。                                           |      |
| `'o'`  | 有符号八进制数。                                             | (1)  |
| `'u'`  | 过时类型 -- 等价于 `'d'`。                                   | (6)  |
| `'x'`  | 有符号十六进制数（小写）。                                   | (2)  |
| `'X'`  | 有符号十六进制数（大写）。                                   | (2)  |
| `'e'`  | 浮点指数格式（小写）。                                       | (3)  |
| `'E'`  | 浮点指数格式（大写）。                                       | (3)  |
| `'f'`  | 浮点十进制格式。                                             | (3)  |
| `'F'`  | 浮点十进制格式。                                             | (3)  |
| `'g'`  | 浮点格式。 如果指数小于 -4 或不小于精度则使用小写指数格式，否则使用十进制格式。 | (4)  |
| `'G'`  | 浮点格式。 如果指数小于 -4 或不小于精度则使用大写指数格式，否则使用十进制格式。 | (4)  |
| `'c'`  | 单个字符（接受整数或单个字符的字符串）。                     |      |
| `'r'`  | 字符串（使用 [`repr()`](https://docs.python.org/zh-cn/3.9/library/functions.html#repr) 转换任何 Python 对象）。 | (5)  |
| `'s'`  | 字符串（使用 [`str()`](https://docs.python.org/zh-cn/3.9/library/stdtypes.html#str) 转换任何 Python 对象）。 | (5)  |
| `'a'`  | 字符串（使用 [`ascii()`](https://docs.python.org/zh-cn/3.9/library/functions.html#ascii) 转换任何 Python 对象）。 | (5)  |
| `'%'`  | 不转换参数，在结果中输出一个 `'%'` 字符。                    |      |

注释:

1. 此替代形式会在第一个数码之前插入标示八进制数的前缀 (`'0o'`)。

2. 此替代形式会在第一个数码之前插入 `'0x'` 或 `'0X'` 前缀（取决于是使用 `'x'` 还是 `'X'` 格式）。

3. 此替代形式总是会在结果中包含一个小数点，即使其后并没有数码。

   小数点后的数码位数由精度决定，默认为 6。

4. 此替代形式总是会在结果中包含一个小数点，末尾各位的零不会如其他情况下那样被移除。

   小数点前后的有效数码位数由精度决定，默认为 6。

5. 如果精度为 `N`，输出将截短为 `N` 个字符。

6. 参见 [**PEP 237**](https://www.python.org/dev/peps/pep-0237)。

由于 Python 字符串显式指明长度，`%s` 转换不会将 `'\0'` 视为字符串的结束。

*在 3.1 版更改:* 绝对值超过 1e50 的 `%f` 转换不会再被替换为 `%g` 转换。