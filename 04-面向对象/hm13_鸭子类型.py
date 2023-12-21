"""
一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟可以被称为鸭子。这就是鸭子类型Duck Typing

1. someone_eat需要传递一个具备eat方法的对象，但是Dog也具备eat功能,所以也可以传递运行
2. 这是由于python是动态类型语言，不能像C++、Java等静态类型语言一样，限制传递的数据类型
3. 只要运行时发现dog对象有这个功能，就可以在函数中使用
"""


class Dog:

    def eat(self):
        print("狗吃骨头")

    def gaga(self):
        print("嘎嘎叫")

    def wangwang(self):
        print("wangwang")


class Duck:

    def eat(self):
        print("鸭子吃虫子")

    def gaga(self):
        print("鸭子嘎嘎叫")

    def haha(self):
        print()


# 函数
def someone_eat(someone):
    """
    接收一个具备吃eat功能的对象
    接收一个具备吃gaga功能的对象
    """
    someone.eat()
    someone.gaga()


duck = Duck()
someone_eat(duck)

dog = Dog()
someone_eat(dog)
