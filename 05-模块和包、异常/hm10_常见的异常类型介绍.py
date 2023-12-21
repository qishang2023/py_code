def index_error():
    # 角标越界异常
    lst = [10, 20, 30]
    print(lst[6])


def key_error():
    # KeyError 字典中 的键不存在
    d = {'name': '张三', 'age': 30}
    print(d['phone'])


def value_error():
    num = "123abc"
    rst = int(num)
    print(rst)


class Person:
    def __init__(self):
        self.name = '张三'
        self.age = 30


def attr_error():
    p = Person()
    print(p.id)


# index_error()
# key_error()
value_error()
# attr_error()
