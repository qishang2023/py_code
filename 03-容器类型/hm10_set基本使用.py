"""
# 1. 集合定义： {元素1, 元素2, 元素3}
# 2. 集合作用：去重，元素唯一
# 3. 遍历 for in
# 4. 添加： 集合.add(元素)
# 5. 删除
    集合.remove(元素)   # 元素不存在报错
    集合.pop()    # 随机删除
    集合.discard(元素)  # 删除元素 如果元素不存在,不做任何处理
"""

temp = {}
print(type(temp))
temp = {1, 2}
print(type(temp))
temp = {1: 1, 2: 2, 3: 3}
print(temp,type(temp))
