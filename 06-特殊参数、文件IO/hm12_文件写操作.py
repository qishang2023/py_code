"""
# 1. 打开文件，只写方式打开
# 2. 写文件
# 3. 关闭文件

需求：往文件，写入 'hello python\n'， 'hello mike\n', 'hello abc\n'三句话
文件变量.write(内容)
"""
with open('hello.txt', 'w') as f:
    f.write('hello python\n')
    f.write('hello mike\n')
    f.write('hello abc\n')

