"""
角色：石头 1， 剪刀 2， 布 3
玩家：
    用户：user
    电脑：computer
用户赢的情况：
    user == 1 and computer == 2
    user == 2 and computer == 3
    user == 3 and computer == 1
平局：
    user == computer
else:
    电脑赢

流程
# 1. 输入用户的角色
# 2. 电脑随机出石头、剪刀、布
# 3. 判断
"""
from random import *

user = int(input("请输入您的角色：1：石头，2：剪刀，3：布\n"))
computer = randint(1, 3)
print('电脑出的是：', computer)
if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print('你赢了')
elif user == computer:
    print('平局')
else:
    print('你输了')
