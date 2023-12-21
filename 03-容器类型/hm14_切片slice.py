"""
说明: 通过切片操作, 可以获取数据中指定部分的内容
    - 适用类型: 字符串(str)/列表(list)/元组(tuple)
语法: 数据[起始索引:结束索引:步长]
0. 步长默认为1，步长理解为走几步，正数从左往右取数，负数从右往左取数
1. 字符串[开始索引:结束索引] 开始索引 ~（结束索引-1）
2. 字符串[开始索引: ] 开始索引 ~ 末尾最后一个元素，末尾索引不写，默认能取到末尾那个索引
3. 字符串[ :结束索引] 0 ~（结束索引-1），开始索引不写，如果步长为1，默认从第0个元素开始

str_data = 'abcdefg'
#           0123456

# 1. 取出 cde
# 2. 取出 abcde
# 3. 取出 bcdefg
# 4. 取出 aceg
# 5. 取出 fg
# 6. 字符串翻转，逆向输出 gfedcba
"""
str_data = 'abcdefg'
#           0123456
# 1. 取出 cde
print(str_data[2:5])
# 2. 取出 abcde
print(str_data[:5])
# 3. 取出 bcdefg
print(str_data[1:])
# 4. 取出 aceg
print(str_data[::2])
# 5. 取出 fg
print(str_data[5:])
# 6. 字符串翻转，逆向输出 gfedcba
print(str_data[::-1])