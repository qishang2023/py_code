"""
# 1. 打开文件，只读方式打开，'r'
# 'r'： 打开文件，必须存在，不存在，报错崩溃
# 2. 读取文件内容
# 格式： 内容变量 = 文件变量.read(读取的长度)
#       如果read的长度不指定，默认读取全部
"""

with open("./hello.txt",encoding="utf-8") as f:
    content = f.read(5)
    print(content)
    content = f.read(5)
    print(content)
    content = f.read()
    print(content)