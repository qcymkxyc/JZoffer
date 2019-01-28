#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-24 上午11:42
    @Author:  qcymkxyc
    @File: book2.py
    @Software: PyCharm
    
    
"""

def _middle_num(nums):
    """中位数

    :param nums:
    :return:
    """
    nums = sorted(nums)
    if len(nums) % 2 == 0:
        num = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1] ) / 2
    else:
        num = nums[len(nums) // 2]
    return num

def repeat_num(nums):
    """

    :param nums: List[int]
        数组
    :return: int
        重复的数
    """
    def _num_count(middle_num,inner_nums):
        less_list = list()
        great_list = list()
        for i, num in enumerate(inner_nums):
            if num < middle_num:
                less_list.append(num)
            elif num > middle_num:
                great_list.append(num)

        return less_list, great_list

    if len(nums) == 0 or len(nums) == 1:
        raise ValueError("无重复数字")

    middle_num = _middle_num(nums)
    less_list, great_list = _num_count(middle_num,nums)
    if len(less_list) + len(great_list) < len(nums) - 1:
        return middle_num
    if len(less_list) > len(great_list):
        return repeat_num(less_list)
    else:
        return repeat_num(great_list)






