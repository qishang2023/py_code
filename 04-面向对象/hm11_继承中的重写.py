"""
重写：重新写(定义)一次父类的同名方法
为什么需重写：父类同名方法不满足需求
子类如何调用父类同名方法：super().父类同名方法(参数)

父类名：Person
实例属性：name, age
实例方法：
    __init__() 添加实现属性
    say_hello() 打印 xxx say hello，今年 xxx 岁

子类名：Student 继承于 Person类
实例属性：新增score
实例方法：
    重写__init__()方法：调用父类的__init__，再增加score
    go_school(): 打印： xxx 去考试，得分：xxx
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'{self.name} say hello，今年 {self.age} 岁')


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def go_school(self):
        print(f'{self.name} 去考试，得分：{self.score}')


s1 = Student('张三', 18, 100)
s1.go_school()
s1.say_hello()
