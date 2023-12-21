"""
增：
    字典[不存在的键] = 新的值
删：
    del 字典[键]   # 键不存在，报错
    字典.pop(键)   # 键不存在，报错
    字典.clear()   # 清空字典
改：
    字典[存在的键] = 新的值
查：
    字典[键]       # 键不存在，报错
    字典.get(键)   # 键不存在，返回None
"""

dict1 = {"name": "Tom", "age": 18, "gender": "male"}
print(dict1)
print('=' * 20 + '增和改'+'=' * 20)
dict1["address"] = "北京"
print(dict1)
dict1["name"] = "jack"
print(dict1)


print('=' * 20 + '删'+'=' * 20)
del dict1["address"]
print(dict1)
dict1.pop("age")
print(dict1)
# dict1.clear()
# print(dict1)


print('=' * 20 + '查'+'=' * 20)
print(dict1["name"])
print(dict1.get("name"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
