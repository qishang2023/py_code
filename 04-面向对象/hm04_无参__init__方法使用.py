"""
__init__方法(双下划线，不是单下划线)：
    1. 作用：初始化，添加属性
        self.属性变量名 = 内容
    2. 特点：创建对象的时候，实例化对象，自动调用__init__方法

类名：Person
属性：name
方法：
    __init__(): 添加属性，属性内容为'小明'
    eat(): 打印xx爱吃饭， xx替换为具体的属性
"""


class Person:
    def __init__(self):
        print("无参构造方法")

    def eat(self):
        print("%s爱吃饭" % self.name)


p1 = Person()
p1.name = "小明"
p1.eat()
