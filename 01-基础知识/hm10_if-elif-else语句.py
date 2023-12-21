"""
if-elif-else语法:
if 条件1:
    条件1满足时执行的代码
elif 条件2:
    条件2满足时执行的代码
elif 条件n:
    条件n满足时执行的代码
else:
    以上条件均不满足时执行的代码
注意：
1. 从上往下判断
2. 满足某个条件后，执行满足条件的代码，其它条件不再判断执行

需求：
1. 定义 holiday_name 字符串变量记录节日名称
2. 如果是 情人节，应该 买玫瑰／看电影
3. 如果是 平安夜，应该 买苹果／吃大餐
4. 如果是 生日，应该 买蛋糕
5. 其他的日子，每天都是节日……
"""
holiday_name = input("请输入节日名称:")
if holiday_name == "情人节":
    print("买玫瑰/看电影")
elif holiday_name == "平安夜":
    print("买苹果/吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("每天都是节日")
