#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-23 上午11:02
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


def check_power(part_power):
    """检测幂部分是否正确

    主要检测两个问题：
    1. 幂无数字
    2. 包含小数点

    :param part_power: str
        幂部分
    :return: bool
        是否正确
    """
    # 如果无幂部分
    if part_power == "":
        return True
    # 如果e后面无任何字符
    if part_power[1:] == "":
        return False

    part_power = part_power[1:]     # 去掉e
    power_signal = part_power[0] if part_power[0] in "+-" else ""   # 幂符号
    part_power = part_power if power_signal == "" else part_power[1:]    # 幂部分

    # 无数字问题
    have_num = False
    for ch in part_power:
        if ord("0") <= ord(ch) <= ord("9"):
            have_num = True
            break
    if not have_num:
        return False
    # 包含小数点
    if "." in part_power:
        return False

    return True


def check_num(part_num):
    """检测数值部分

    检测数值部分是否正确，错误包括:
    1. 数值部分为空
    2. 多符号
    3. 多小数点
    4. 无数字

    :param part_num: str
        数值部分（包含符号）
    :return: bool
        是否正确
    """
    # 数值部分为空
    if part_num == "":
        return False

    num_signal = part_num[0] if part_num[0] in "+-" else ""     # 数值符号
    part_num = part_num if num_signal == "" else part_num[1:]   # 数值部分

    # 多符号问题
    if "+" in part_num or "-" in part_num:
        return False
    # 多小数点问题
    point_index = part_num.find(".")
    if point_index != -1 and "." in part_num[point_index + 1:]:
        return False
    # 无数字问题
    have_num = False
    for ch in part_num:
        if ord("0") <= ord(ch) <= ord("9"):
            have_num = True
            break
    if not have_num:
        return False

    return True


def is_num(string):
    """判断string是否可以转换成数字

    错误的情况包括：
    1. 包含除e之外的字母
    2. 多个小数点
    3. 指数包含小数点
    4. e后面无指数
    5. 多符号
    6. e前面无数字

    :param string: str
        string
    :return: bool
        是否可以转换
    """
    string = string.lower()

    # 包含字符是否正确
    for i, ch in enumerate(string):
        if not (ord("0") <= ord(ch) <= ord("9") or ch in "e+-."):
            return False

    e_index = string.find("e")
    part_num = string if e_index == -1 else string[:e_index]    # 数值部分（包含符号）
    part_power = "" if e_index == -1 else string[e_index:]      # 幂部分（包含符号及e）

    return check_power(part_power) and check_num(part_num)
