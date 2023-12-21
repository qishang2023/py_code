"""
内置方法：
    len(items)	计算容器中元素个数
    del item	删除变量
    max(items)	返回容器中元素最大值	字典只比较key
    min(items)	返回容器中元素最小值	字典只比较key
运算符：
    +	合并	字符串、列表、元组
    *	重复	字符串、列表、元组
    in	是否存在(字典中判断键)	字符串、列表、元组、集合、字典
    not in	是否不存在(字典中判断键)	字符串、列表、元组、集合、字典
    > >= == < <=	比较（==以外的较少使用，逐个比较元素）	字符串、列表、元组
"""

_str = 'hello'
print(len(_str))

lst = [1, 2, 3, 4, 5]
# 根据索引删除
del lst[2]
print(lst)
print("----------------------内置函数")
lst = [3, 4, 1, 54, -3, 66, 14]
lst = (3, 4, 1, 54, -3, 66, 14)
lst = {4, 4, 1, 54, -3, 66, 14}
lst = {12: "ab", 43: "acd", 2: "abdd"}
print("最大值：", max(lst))
print("最小值：", min(lst))

print(max(23, 133, 12))
print(min(23, 133, 12))

print("---------------------合并")
a = [1, 2, 3]
b = [6, 7, 8]
print(a + b)

print("---------------------重复")
print(a * 3)
print(_str * 3)

print("---------------------not in")
print(1 in a)
print(9 in a)
print(9 not in a)

print("---------------------比较")
# 逐个比较
a = [1, 2, 300]
b = [7, 2, 1]
print(a == b)
print("a > b:", a > b)
print("a < b:", a < b)

print("---------------------字符串的比较ASCII")
# 根据字符在ASCII码表里的顺序逐个比较
a_str = "hella"
b_str = "hello"
print(a_str > b_str)
