#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-30 上午10:31
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my_sort.py
@Software: PyCharm

排序练习
    
"""
import copy

def quick_sort(nums):
    """快速排序

    :param nums: list or tuple
        输入序列
    :return: list
        排序结果
    """
    sort_list = copy.copy(list(nums))



    def patition(nums):
        """

        :param nums:
        """
        x = nums[0]

        i,j = 0,len(nums) - 1
        while i < j:
            while nums[j] > x and j > i:
                j -= 1
            nums[i] = nums[j]
            while nums[i] < x and i < j:
                i += 1
            nums[j] = nums[i]
        nums[i] = x;








