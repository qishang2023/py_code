"""
增：
    列表.append(元素)
删：
    列表.pop(元素索引)
    列表.remove(元素)
改：
    列表[索引] = 新内容
查：
    列表[索引]
找：
    列表.index(元素) 返回元素所在的位置
排序：
    升序：列表.sort()
    降序：列表.sort(reverse=True)
反转：
    列表.reverse()
"""
num_list = [1,3,5,7,2,4,6,8]
print(num_list)
print("="*50 + "增")
num_list.append(9)
print(num_list)
print("="*50 + "删")
num_list.pop(0)
print(num_list)
num_list.remove(3)
print(num_list)
print("="*50 + "改")
num_list[0] = 0
print(num_list)
print("="*50 + "找")
print(num_list.index(4))
print("="*50 + "排序")
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
print("="*50 + "反转")
num_list.reverse()
print(num_list)
