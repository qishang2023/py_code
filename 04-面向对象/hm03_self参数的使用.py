"""
1. self是什么？
    谁调用方法，self就是那个谁
    tom对象调用eat方法，self就是tom对象
2. 如何访问属性和方法
    类方法里面： self.属性、self.方法()
    类外面：    对象变量名.属性、对象变量名.方法()
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
