"""
# 需求:
# 1. 定义一个函数 sum_numbers， 可以接收的 任意多个整数
# 2. 功能要求： 将传递的 所有数字累加 并且返回累加结果
"""


def func(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print("sum=", func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
