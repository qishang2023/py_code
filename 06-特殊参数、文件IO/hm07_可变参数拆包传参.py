# 在调用函数参数时, 实参加 * , 代表把实参的内容拆分后再传递，为拆包操作
# 函数调用， 实参加 **, 代表把实参的内容拆分分后再传递，为拆包操作

def func1(*args):
    print(args, type(args))


def func2(**kwargs):
    print(kwargs, type(kwargs))


t1 = (1, 2, 3, 4, 5)
t2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

func1(*t1)
func2(**t2)
