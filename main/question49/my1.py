#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-28 上午10:32
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def ugly_num(order):
    """丑数

    :param order: int
        第多少个
    :return: int
        对应的数字
    """
    ugly_nums = [1]
    last_nums = [1]

    def _find_ugly_num(pre_nums):
        temp = []
        for v in pre_nums:
            temp.append(v * 2)
            temp.append(v * 3)
            temp.append(v * 5)

        ugly_nums.extend(temp)
        return temp

    while len(ugly_nums) < order:
        last_nums = _find_ugly_num(last_nums)

    print(len(ugly_nums))
    return sorted(ugly_nums)[order - 1]
