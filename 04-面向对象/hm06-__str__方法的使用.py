"""
__str__方法:
    0. 作用：方便打印对象的属性信息
    1. 返回值必须是字符串类型，不是返回print
    2. print(对象变量名)  对象变量名的位置替换为__str__()方法返回值的内容
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'我叫{self.name},今年{self.age}岁了'


p1 = Person('张三', 18)
print(p1)
