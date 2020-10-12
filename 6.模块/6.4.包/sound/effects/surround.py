from . import echo # 依然在main.py执行，但是这里可以调用同目录下的兄弟模块
from .. import formats # 可以调用父包里面的兄弟子包
from ..filters import equalizer #可以调用兄弟子包中的模块 

## 相对引入

echo.echofilter()

equalizer.foo()