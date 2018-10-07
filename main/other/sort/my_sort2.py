#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-7 下午12:26
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my_sort2.py
@Software: PyCharm

排序第二次训练
    
"""

##############################################################
#   插入排序
###############################################################
def insert_sort(nums):
    """直接插入排序

    :param nums: list
        待排数组
    """
    for i in range(1,len(nums)):
        current_num = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] < current_num:
                break
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current_num
