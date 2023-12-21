"""
class 自定义异常名(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

# 抛出异常
raise 异常类型名(提示信息)
"""


class MyException(Exception):
    def __init__(self, msg):
        """
        异常的提示文字
        :param msg:
        """
        self.msg = msg

    def __str__(self):
        return self.msg

print('开始1111111111')
# 抛出异常
raise MyException('出现了0')
print('结束2222222222')
