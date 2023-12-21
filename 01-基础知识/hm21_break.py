"""
# break：某一条件满足时，不再执行循环体中后续代码，并退出循环
# 需求: 一共吃5碗饭, 吃到第3碗吃饱了, 结束吃饭动作
"""
for i in range(1, 6):
    print("第%d碗饭" % i)
    if i == 3:
        print("吃饱了")
        break
    print("吃完了第%d碗饭" % i)
