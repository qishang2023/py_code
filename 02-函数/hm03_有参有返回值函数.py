"""
函数返回值作用：想使用函数内某个数据, 需要使用 return 关键字返回结果
return关键字：结束函数，也可以同时返回一个结果
函数定义格式：
def 函数名():
    return 结果

函数调用格式：
返回值变量 = 函数名()
"""



def myadd(a, b):
    """
    Add two numbers together and return the result.

    :param a: The first number to be added.
    :type a: int or float
    :param b: The second number to be added.
    :type b: int or float
    :return: The sum of the two numbers.
    :rtype: int or float
    """
    return a + b

print(myadd(1, 2))
