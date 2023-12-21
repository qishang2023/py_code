"""
__init__方法(双下划线，不是单下划线)：
    1. 作用：添加属性
    2. 特点：创建对象的时候，实例化对象，自动调用__init__方法
    3. 设置参数，创建对象时，除了self参数不用人为处理，其它参数需要和__init__参数匹配
        对象名 = 类名(实参1， 实参2) ====》 __init__(self, 形参1, 形参2)
"""

class Person:

    def __init__(self, name="Tom", age=18):
        print("有参构造方法")
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃饭" % self.name)


p1 = Person()
p1.eat()

p2 = Person("Jerry", 20)
p2.eat()