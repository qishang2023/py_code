"""
# 1. 列表定义 列表变量的名字 = [元素1, 元素2, ……]
# 2. 列表元素访问 列表[索引]
# 3. 列表遍历
"""
name_list = ['张三', '李四', '王五', '赵六']
print(name_list,type(name_list))
print(name_list[3],name_list[-1],type(name_list[3]))
for name in name_list:
    print(name,type(name))
print(name_list.count('张三'))