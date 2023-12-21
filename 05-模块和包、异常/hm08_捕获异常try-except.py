"""
try:
    可能发生异常的代码
except Exception as 异常对象名:
    # Exception : 为系统提供的异常类, 凡是未知错误类型, 都可以尝试使用该异常类进行异常类型匹配
    print(异常对象名) 即可获取异常的信息描述

说明：
1. 如果希望程序无论出现任何错误， 都不会因为Python解释器抛出异常而被终止， 可以捕获 Exception
2. except Exception as e: e表示捕获到的异常对象， 记录异常的错误信息， e为惯用变量名， 可以自定义

需求：
1. 提示用户输入一个整数
    - 用户输入的可能不是一个整数
2. 使用 8 除以用户输入的整数并且输出
    - 0不能做除数
"""

try:
    num = int(input("请输入一个整数: "))
    print(8 / num)
except Exception as e:
    print("发生了异常，异常原因：", e)
print("程序结束")
