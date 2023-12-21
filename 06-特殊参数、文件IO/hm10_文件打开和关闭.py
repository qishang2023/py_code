"""操作文件的流程：
1. 打开文件
2. 读或写文件
3. 关闭文件

打开文件格式：
    文件变量 = open(文件名字，访问模式, encoding='utf-8')
注意：
1. 文件名字，访问模式都是字符串类型
2. 如果操作文本文件，encoding='utf-8'为指定utf-8编码，防止不同平台中文乱码
    - 这个当做结论记
"""
# f = open("../test.txt", 'r', encoding='utf-8')
f = open("test.txt", 'w', encoding='utf-8')

f.close()
