"""
通过as重命名，可以解决冲突
from 模块名 import 变量 as 别名1, 函数 as 别名2, 类 as 别名3
"""

from demo import name as u_name, sum as u_sum
from utils import name, sum

print(u_name)
print(u_sum(1, 2))
print(name)
print(sum(10, 20))


if __name__ == '__main__':
    print('我是主程序')