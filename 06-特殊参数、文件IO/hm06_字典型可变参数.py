"""
1. 函数形参变量的前面加一个**， 这个参数则为字典型不定长参数
2. **kwargs : 用于接收字典类型数据, kwargs 为习惯命名, 可以自定义
3. 在函数内使用形参，无需加*
4. 函数调用，字典型不定长参数使用关键字传参
"""


def func(**kwargs):
    print(kwargs, type(kwargs))


func()
func(a=1, b=2, c=3)
