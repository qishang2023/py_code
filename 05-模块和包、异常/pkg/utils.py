# 定义变量
name = '张三'


# 定义函数
def sum(a, b):
    return a + b


# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name:{}, age:{}'.format(self.name, self.age)


print("条件外面__name__:", __name__)

if __name__ == '__main__':
    # 把导入模块不被执行的代码放在if __name__ == '__main__'里面
    print("条件里面__name__:", __name__)
