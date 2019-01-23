#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-23 上午11:29
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm
    
    
"""


def repeat_num(nums):
    """查找相同数

    :param nums: List[int]
        数组
    :return: bool
        是否有相同数
    """
    # 数不合规范
    if max(nums) >= len(nums):
        raise ValueError

    for i in range(len(nums)):
        current_num = nums[i]
        while current_num != i:
            num1 = nums[current_num]
            # 如果找到两个数相同
            if num1 == current_num:
                return True
            else:
                nums[i], nums[current_num] = nums[current_num], nums[i]
                current_num = nums[i]

    return False

