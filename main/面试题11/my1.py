#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-7 上午11:03
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""

def find_min(nums):
    """查找最小数

    :param nums:list
        旋转数组
    :return:int
        最小数
    """
    for i in range(1,len(nums)):
        if nums[i] < nums[i - 1]:
            return nums[i]