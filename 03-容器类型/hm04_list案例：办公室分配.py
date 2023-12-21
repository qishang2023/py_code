"""
需求
一个学校，有3个办公室，现在有8位老师等待工位的分配
['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']

请编写程序:
1. 完成随机的分配
2. 打印办公室信息 (每个办公室中的人数，及分别是谁)

分析：
1. 定义3个办公室的列表：列表嵌套
2. 声明8位老师到列表中
3. 遍历老师的列表
4. 随机存放到办公室中
"""
from random import randint

teacher_list = ['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']
office_list = [[], [], []]
i = 0
while i < len(teacher_list):
    office = randint(0, 2)
    if len(office_list[office]) == 3:
        continue
    office_list[office].append(teacher_list[i])
    i += 1
print(office_list)
