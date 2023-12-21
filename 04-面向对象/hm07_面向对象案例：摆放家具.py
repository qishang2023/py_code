"""
需求：
1. 房子(House) 有 户型、 总面积、剩余面积 和 家具名称列表
    - 新房子没有任何的家具、剩余面积和总面积相等
2. 家具(HouseItem) 有 家具名字 和 家具面积， 其中
    - 席梦思(bed) 占地 4 平米
    - 衣柜(chest) 占地 2 平米
    - 餐桌(table) 占地 1.5 平米
3. 将以上三件 家具 添加 到 房子 中
    - 向房间 添加家具 时， 让 剩余面积 -= 家具面积
4. 打印房子时， 要求输出： 户型、 总面积、 剩余面积、 家具名称列表

家具类
类名：HouseItem
属性：家具名称name、家具面积area
方法：
    __init__(): 添加属性
    __str__(): 以字符串格式返回属性信息


房子类
类名：House
属性：户型house_type、 总面积area、剩余面积free_area 和 家具名称列表item_name_list
方法：
    __init__(): 添加属性
    __str__(): 以字符串格式返回属性信息
    add_item(): 添加家具，需要一个形参house_item接收家具对象
"""


class Item:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具名称：{self.name}, 家具面积：{self.area}'


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return (f'户型：{self.house_type}, 总面积：{self.area}, '
                f'剩余面积：{self.free_area}, 家具名称列表：{self.item_list}')

    def add_item(self, item):
        if item.area > self.free_area:
            print(f'剩余面积不足，无法添加 {item.name}，当前剩余面积为 {self.free_area}')
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


# - 席梦思(bed) 占地 4 平米
bad = Item('席梦思', 4)
print(bad)
# - 衣柜(chest) 占地 2 平米
chest = Item('衣柜', 2)
print(chest)
# - 餐桌(table) 占地 1.5 平米
table = Item('餐桌', 1.5)
print(table)

house1 = House('两室一厅', 60)
house1.add_item(bad)
house1.add_item(chest)
house1.add_item(table)
print(house1)
