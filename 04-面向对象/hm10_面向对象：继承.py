"""
继承：复用代码，继承过来的东西可以复用，描述类和类之间的关系
格式：
class 子类名(父类名)：
    pass

# 父类，也叫基类
# 子类，也叫派生类

父类名：Person
实例属性：name, age
实例方法：
    __init__() 添加实现属性
    say_hello() 打印 xxx say hello，今年 xxx 岁

子类名：Student 继承于 Person类
类里面没有实现任何功能
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'{self.name} say hello，今年 {self.age} 岁')


class Student(Person):
    pass


s1 = Student('张三', 18)
s1.say_hello()
