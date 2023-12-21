"""
需求：
● 用户名和密码格式校验程序
● 要求从键盘输入用户名和密码，分别校验格式是否符合规则
    ○ 如果符合，打印用户名合法，密码合法
    ○ 如果不符合，打印出不符合的原因，并提示重新输入
● 用户名长度6-20，用户名必须以字母开头
● 密码长度至少6位，不能为纯数字，不能有空格

分析：
1.从键盘输入用户名(需要while循环)
2.长度6-20
3.必须字母开头

4.输入密码(while循环)
5.密码长度至少6位
6.不能为纯数字
7.不能有空格
"""
name = input("请输入用户名:")
while True:
    if len(name) < 6 or len(name) > 20:
        print("用户名长度不符合要求，长度为6~20")
        name = input("请重新输入用户名:")
    elif not name[0].isalpha():
        print("用户名必须以字母开头")
        name = input("请重新输入用户名:")
    else:
        print("用户名符合要求")
        break

pwd = input("请输入密码:")
while True:
    if len(pwd) < 6:
        print("密码长度不符合要求，不能少于6位")
        pwd = input("请重新输入密码:")
    elif pwd.isdigit():
        print("密码不能为纯数字")
        pwd = input("请重新输入密码:")
    elif " " in pwd:
        print("密码不能有空格")
        pwd = input("请重新输入密码:")
    else:
        print("密码符合要求")
        break
