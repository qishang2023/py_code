"""
定义类格式：
# Python3以后，3种写法完全等价
#class 类名:
#class 类名():
class 类名(object): # 新式类写法，object所有类的祖先
    方法的定义

注意：类名 建议 大驼峰命名法

类的设计
类名: 人类(Person)
属性: 无
方法: 吃饭(eat)/运动(run)

1. 定义类，只是定义了一个类型
2. 根据类创建对象（实例化对象）， 通过设计图创建一个实物
    格式：  实例对象变量名 = 类名() # 小括号一定不能省略
3. 类外面方法如何调用
    对象变量.方法名字()
"""


class Person(object):
    pass

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃饭" % self.name)

    def run(self):
        print("%s在跑步" % self.name)


p1 = Person("张三", 18)
p1.eat()
p1.run()
