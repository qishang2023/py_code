"""
# readline 方法可以一次读取一行内容, 想要读取完全部内容, 一般会配合循环使用!
# 1. 只读方式打开文件
# 2. 死循环
# 3. 读取1行内容，data接收返回值
# 4. if data:  有内容，就是真，非0，非空字符串''，就是真，打印读取的内容
# 5. 否则，说明没有读到内容，说明文件读取完毕，跳出循环
"""
with open("./u1s1.txt", encoding="utf-8") as f:
    while True:
        data = f.readline()
        if data:
            print(data, end="")
        else:
            print("文件读取完毕!")
            break
