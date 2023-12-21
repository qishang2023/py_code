"""
需求：
1. 输入一个文件名，统计文件中代码行数、注释行数、空行数
2. 打印代码行数、注释行数、空行数
分析：
1.输入文件名 test.py
2.打开文件
3.统计 readline
    空行 空
    注释行数 去空格 #开头
    代码行数
"""
num1 = 0  # 空行
num2 = 0  # 注释行
num3 = 0  # 代码行
name = input("请输入文件名")
with open(name, encoding='utf-8') as f:
    while True:
        data = f.readline()
        if data:
            if data.startswith('#'):
                num2 += 1
            elif data.startswith('\n'):
                num1 += 1
            else:
                num3 += 1
        else:
            print(name, "文件读取完毕")
            break
print(f"空行：{num1}；注释行：{num2}；代码行：{num3}")
