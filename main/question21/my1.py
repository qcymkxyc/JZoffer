#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-24 上午10:55
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


def adjust_list(nums):
    """调整nums的顺序使奇数位于偶数之前

    用链表的思想，扫描一次nums，如果是奇数在表头插入，如果是偶然
    在表尾插入

    :param nums: list or tuple
        原始数组
    :return: list
        调整后的数组
    """
    adjusts = list()    # 调整后的列表
    for num in nums:
        if num % 2 == 1:
            adjusts.insert(0, num)
        else:
            adjusts.append(num)

    return adjusts
