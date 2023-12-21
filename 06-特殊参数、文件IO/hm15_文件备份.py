"""
1.输入文件名 文件名.py
2.创建文件  文件名[复制].py
3.读取文件, 写入到复制的文件中
"""

name = input("请输入文件名:")
index = name.rfind(".")
name_pre = name[:index]
name_suf = name[index:]
new_name = name_pre + "[复制]" + name_suf
with open(name, encoding="utf-8") as f1, open(new_name, "w", encoding="utf-8") as f2:
    while True:
        data = f1.readline()
        if data:
            f2.write(data)
        else:
            break
