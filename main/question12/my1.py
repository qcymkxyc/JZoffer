#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-8 上午10:59
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


def is_coordinate_right(matrix, coordinate):
    """判断坐标是否正确

    如果坐标越界（比如x<0等情况），则返回False，否则返回True

    :param matrix: list
        要查找的矩阵
    :param coordinate: tuple
        坐标
    :return:bool
        是否正确
    """
    x, y = coordinate
    if y < 0 or y >= len(matrix):
        return False
    if x < 0 or x >= len(matrix[y]):
        return False
    return True


def find_path1(matrix, s):
    """在矩阵中寻找字符串路径

    利用迭代方式查找

    :param matrix: list
        矩阵
    :param s: str
        字符串
    :return: list or None
        如果找到，则返回坐标路径，否则返回None
    :raises:
        ValueError : 矩阵中的字符串长度不一致
    """
    def init_visit_matrix():
        """初始化访问矩阵
        
            矩阵为一个两重list，list的行和列等于要查找的矩阵，
            list中的值为bool类型,所有的状态均为False，表示均未
            经过
        
        :return: list
            访问矩阵
        """

        visit = []
        for row,row_num in enumerate(matrix):
            visit.append([False] * len(row_num))
        return visit

    col_num = None
    for row_num in matrix:
        col_num = len(row_num) if col_num is None else col_num
        if col_num != len(row_num):
            raise ValueError("矩阵格式错误")

    # 搜索起始坐标
    start_ch = s[0]
    start_cordinates = []
    for row,row_num in enumerate(matrix):
        for col,ch in enumerate(row_num):
            if ch == start_ch:
                start_cordinates.append((col,row))

    # 查找路径
    for start_cordinate in start_cordinates:
        # 初始化是否访问矩阵
        is_visit = init_visit_matrix()
        str_path = find_ch(matrix,0,s,start_cordinate,is_visit)
        if str_path :
            return str_path


def find_ch(matrix, index, s, current_cordinate, is_visit):
    """查看字符是否存在

    利用迭代的方式实现，当前寻找的坐标分以下几种情况：
    1. 有边界错误
        1.1 当前坐标出错，比如x<0或x>=len(maxtrix),y同理
        1.2 index出错，index超出字符串的范围
        1.3 该坐标已经访问过
    2. 无边界错误
        2.1 找到要寻找的字符，继续往该结点的四个方向迭代
        2.1 未找到字符，返回None

    :param matrix:list
        要查找的矩阵，list中的每个元素为一个字符串
    :param index: int
        要查找字符的index
    :param s:str
        要查找的字符串
    :param current_cordinate:tuple
        当前坐标
    :param is_visit: list
        表示是否访问的矩阵
    :return: list or None
        如果找到字符，则返回一个包含当前坐标的list，否则返回None
    """
    # 检测有错误的情况

    # 如果坐标不正确
    if not is_coordinate_right(matrix,current_cordinate):
        return
    # 如果index不正确
    if index < 0 or index >= len(s):
        return
    # 该坐标是否已经访问过
    current_x,current_y = current_cordinate
    if is_visit[current_y][current_x]:
        return

    # 无边界错误的情况
    current_ch = s[index]

    # 未找到
    if current_ch != matrix[current_y][current_x]:
        is_visit[current_y][current_x] = False
        return

    # 已找到
    pathes = [current_cordinate]
    is_visit[current_y][current_x] = True

    # 往该结点的四个方向开始找
    close_coordinates = [
        (current_x,current_y - 1),
        (current_x,current_y + 1),
        (current_x - 1,current_y),
        (current_x + 1,current_y)
    ]
    for i, coordinate in enumerate(close_coordinates):
        sub_path = find_ch(matrix,index + 1,s,coordinate,is_visit)
        if sub_path:
            pathes.extend(sub_path)
            break

    # 如果四个方向均未找到且该字符不是最后一个
    if not sub_path and index != len(s) - 1:
        is_visit[current_y][current_x] = False
        return None

    return pathes
