"""
计算器练习需求：
需求:
● 用户输入整型变量a
● 用户输入整形变量b
● 计算输出a+b=?
"""
# a=input('请输入a:')
# b=input('请输入b:')
# print(int(a)+int(b))

"""
超市买苹果计算金额
需求:	
●  收银员输入苹果的价格price，单位：元/斤
●  收银员输入用户购买苹果的重量weight，单位：斤
●   计算并输出付款金额:xxx元
"""
# price= input('请输入苹果的价格：')
# weight= input('请输入用户购买苹果的重量：')
# print(float(price)*float(weight))

"""
在控制台依次提示用户输入：姓名name、公司com、职位title、电话telephone、邮箱email
"""
name = input('请输入姓名:')
com = input('请输入公司:')
title = input('请输入职位:')
telephone = input('请输入电话:')
email = input('请输入邮箱:')

print(50 * '*')
print(f"公司名称：{com}")
print()
print(f"姓名（职位）:{name}({title})")
print()
print(f"电话：{telephone}")
print(f"邮箱：{email}")
print(50 * '*')
