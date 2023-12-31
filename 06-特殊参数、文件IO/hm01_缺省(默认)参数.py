"""
说明：定义函数，形参设定默认值，称为缺省参数，也叫默认参数
特点: 调用函数时, 如果没有传入缺省参数的值, 则使用定义函数时的默认值
作用: 函数的缺省参数, 将常见的值设置为参数的缺省值, 从而简化函数的调用
注意：带有默认值的缺省参数, 必须在所有没有默认值参数的右边(默认参数在后面)
"""


def func(a, b=10, c=20):
    print(f"a={a},b={b},c={c}")


func(100)
func(100, 200)
func(100, 200, 300)
