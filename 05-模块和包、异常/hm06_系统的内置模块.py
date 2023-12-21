import random
import sys
import time
import math  # numpy
from datetime import datetime

if __name__ == '__main__':
    print("-------------------------------sys")
    print(sys.argv)
    print(sys.argv[1:])
    print(sys.path)
    # sys.exit(-2) # 默认结束码是0，非零则有异常

    print("-------------------------------time")
    # 打印当前时间戳
    print(time.time())
    # time.sleep(2)
    # print(time.time())
    print("-------------------------------datetime")
    now = datetime.now()
    print(now)
    print("年：", now.year)
    print("月：", now.month)
    print("日：", now.day)
    print("时：", now.hour)
    print("分：", now.minute)
    print("秒：", now.second)
    print(now.weekday() + 1)
    # string format time
    time_format = "%Y_%m_%d %H:%M:%S"
    strptime = datetime.strftime(now, time_format)
    print(strptime)
    # string parse time
    datetime_strptime = datetime.strptime(strptime, time_format)
    print(datetime_strptime)

    print("----------------------------计算模块")
    aaa = [2, 4, 1, 2, 3, 6]
    # 列表最大值
    print(max(aaa))
    # 列表最小值
    print(min(aaa))
    # 列表和
    print(sum(aaa))
    # 列表长度
    print(len(aaa))
    # 列表排序(得到的是一个新的列表,源列表不变，区别于aaa.sort()）
    print(sorted(aaa))
    # 列表倒序
    print(sorted(aaa, reverse=True))

    print("----------------------------math数学模块")
    print(2 ** 3)
    print(math.pow(2, 3))
    print(math.floor(1.7182123123))
    print(math.ceil(1.3182123123))

    print(round(1.7182123123))
    print(round(1.3182123123))
    print("math.pi: ", math.pi)
    print(math.sin(1.71828))
    print(math.sin(math.pi))  # 0
    print(math.sin(math.pi / 2))  # 1

    print("----------------------------random随机数")
    print(random.randint(2, 5))  # 随机整数 [start,end]
    print(random.random())  # [0, 1)
    print(2 + random.random() * 10)  # [2, 12)
    print(random.uniform(1.3, 2.5))  # [start,end]
    aaa = [2, 4, 1, 2, 3, 6]
    print(random.choice(aaa))  # 取一个值
    print(random.choices(aaa))  # 取一个值，用list包裹
