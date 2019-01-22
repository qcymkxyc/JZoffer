#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-14 上午10:01
    @Author:  qcymkxyc
    @File: question3.py
    @Software: PyCharm

    给定数组arr,返回ａｒｒ的最长子序列长度。比如
    arr = [2,1,5,3,6,4,8,9,7],最长递增子序列为
    [1,3,4,8,9],所以返回这个子序列长度为５
"""


def max_sub_len(nums):
    """最大子序列长度

    :param nums: List[int]
        序列
    :return: int
        长度
    """
    max_len = []    # 保存最长子序列长度
    for i, num in enumerate(nums):
        # 找出比num小的数
        sub_filter = list(filter(lambda x: x < num, nums[:i]))

        if len(sub_filter) == 0:
            max_len.append(1)
            continue

        max_len_index = 0
        for v in sub_filter:
            ind = nums.index(v)
            if max_len[ind] > max_len[max_len_index]:
                max_len_index = ind

        max_len.append(max_len[max_len_index] + 1)

    return max(max_len)
