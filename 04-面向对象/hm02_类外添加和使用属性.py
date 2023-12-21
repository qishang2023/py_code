"""
在类的外面操作对象属性：
1. 创建对象变量(实例化对象)
2. 添加属性：对象.属性 = 内容
    注意：
    1. 第一赋值叫添加属性，下一次赋值叫修改属性
    2. 类外添加属性，了解即可
3. 使用属性：对象变量.属性
"""


class Person:
    def eat(self):
        print("%s在吃饭")

    def run(self):
        print("%s在跑步")


p1 = Person()
p1.name = "张三"
p1.age = 18
print(p1.name)
print(p1.age)
p1.eat()
p1.run()
