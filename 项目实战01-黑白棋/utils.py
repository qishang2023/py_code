
# 标志棋子状态
EMPTY = 0
BLACK = 1
WHITE = 2

def judge_rule(x, y, chess, current_role, eat_chess = True):
    """
    功能：吃子的规则
    :param x: 棋盘x下标
    :param y: 棋盘y下标
    :param chess: 棋子状态数组
    :param current_role: 棋子角色
    :param eat_chess: 默认为True，代表改变原来的数组， False不改变数组内容
    """
    # 棋盘的八个方向
    directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    temp_x, temp_y = x, y
    eat_num = 0

    if chess[temp_x][temp_y] != EMPTY:
        return 0

    for dx, dy in directions:
        temp_x, temp_y = x + dx, y + dy  # 准备判断相邻棋子

        if 0 <= temp_x < len(chess) and 0 <= temp_y < len(chess) and \
                chess[temp_x][temp_y] != current_role and chess[temp_x][temp_y] != EMPTY:

            temp_x, temp_y = x + dx, y + dy  # 继续判断下一个，向前走一步

            while 0 <= temp_x < len(chess) and 0 <= temp_y < len(chess):
                if chess[temp_x][temp_y] == EMPTY:  # 遇到空位跳出
                    break

                if chess[temp_x][temp_y] == current_role:  # 找到自己的棋子，代表可以吃子
                    if eat_chess:  # 确定吃子
                        chess[x][y] = current_role  # 开始点标志为自己的棋子

                        # 添加范围检查，确保不越界
                        while 0 <= temp_x < len(chess) and 0 <= temp_y < len(chess) and \
                                (temp_x, temp_y) != (x, y):
                            chess[temp_x][temp_y] = current_role  # 标志为自己的棋子
                            temp_x, temp_y = temp_x - dx, temp_y - dy  # 继续后退一步
                            eat_num += 1  # 累计
                    else:  # 不吃子，只是判断这个位置能不能吃子
                        temp_x, temp_y = temp_x - dx, temp_y - dy  # 后退一步

                        # 添加范围检查，确保不越界
                        while 0 <= temp_x < len(chess) and 0 <= temp_y < len(chess) and \
                                (temp_x, temp_y) != (x, y):
                            temp_x, temp_y = temp_x - dx, temp_y - dy  # 继续后退一步
                            eat_num += 1
                    break  # 跳出循环

                temp_x, temp_y = temp_x + dx, temp_y + dy  # 向前走一步

            # 如果这个方向不能吃子，就换一个方向
            temp_x, temp_y = x, y

    return eat_num  # 返回能吃子的个数