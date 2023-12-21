"""
# 1. 字符串定义：一对引号(单、双、三)包含
# 2. 获取字符串中元素：字符串[索引]
# 3. 遍历字符串
"""

str1 = "hello"
print(str1[1])
print(hex(id(str1)))
str1 = """# 3. 遍历字符串"""
print(hex(id(str1)))
for i in str1:
    print(f"字符串中的元素：{i}")