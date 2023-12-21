"""
1. 遍历字典的键
# for 任意变量 in 字典变量：
for 任意变量 in 字典变量.keys(): # 和上面等价
    任意变量保存的是字典的键

2. 遍历字典的值
for 任意变量 in 字典变量.values():
    任意变量保存的是字典的值

3. 遍历字典的键和值
for 任意变量1, 任意变量2 in 字典变量.items():
    任意变量1保存的是字典的键
    任意变量2保存的是字典的值
"""
dict1 = {"name": "Tom", "age": 18, "gender": "male"}
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key, value in dict1.items():
    print(key, value)
