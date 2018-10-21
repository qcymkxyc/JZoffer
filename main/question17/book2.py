#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-20 下午12:42
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book2.py
@Software: PyCharm
    
"""
from main.question17 import book1


def order_display(n):
    """顺序打印n位数

    :param n: int
        n位数
    :return : list
        打印结果
    """
    nums = list()
    sub_display(nums, "", n, 0)

    nums.pop(0)
    # 去除前面的0
    book1.delete_zero(nums, n)
    return nums


def sub_display(nums, num, n, index):
    """迭代打印数组

    :param nums: list
        打印结果
    :param num: str
        前面叠加的字符串
    :param n: int
        n位数
    :param index: int
        迭代的index
    """
    if index == n:
        nums.append(num)
        return

    for i in range(0, 10):
        sub_display(nums, num + str(i), n, index + 1)
