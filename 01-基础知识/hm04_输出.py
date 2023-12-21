"""
基本输出：
    print(数据1, 数据2 ……)
格式化输出：
    # 右边的数据按顺序依次放在左边的{}中
    print('{},{}'.format(数据1，数据2))
    # 直接输出{}里面的数据，f也可以写成大写的F，Python3.6及以上解释器才支持
    print(f'{数据1},{数据2}')

需求：
# 1. 定义3个变量，分别保存姓名'mike'，年龄35，城市'sz'
# 2. 格式化输出：姓名：mike，年龄：35，城市：sz
"""

print('姓名：mike，年龄：35，城市：sz')
name = "qs"
age = 18
city = "wh"
print(f'姓名：{name},年龄：{age},城市：{city}')
print("name:", name, "age:", age, "city:", city)
