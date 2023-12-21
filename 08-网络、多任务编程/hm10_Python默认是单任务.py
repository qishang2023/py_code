"""
singing(): 循环5次，每隔0.5s, 打印一次唱歌
dancing(): 循环5次，每隔0.5s, 打印一次跳舞
"""


import time


def singing():
    for i in range(5):
        print("唱歌...", i)
        time.sleep(0.5)


def dancing():
    for i in range(5):
        print("跳舞...", i)
        time.sleep(0.5)


if __name__ == '__main__':
    singing()
    dancing()
