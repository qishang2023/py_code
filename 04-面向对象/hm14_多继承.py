"""
1. 当一个类从多个父类继承属性和方法时，就称为多继承。
2. 多继承格式:
class 子类(父类1,父类2...)
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying.")


class Swimmable:
    def swim(self):
        print(f"{self.name} is swimming.")


class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)


duck = Duck("Donald")
duck.eat()  # 输出: Donald is eating.
duck.sleep()  # 输出: Donald is sleeping.
duck.fly()  # 输出: Donald is flying.
duck.swim()  # 输出: Donald is swimming.
