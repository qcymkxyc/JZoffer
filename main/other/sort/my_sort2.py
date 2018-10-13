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
    for i in range(1, len(nums)):
        current_num = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] < current_num:
                break
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current_num


def binary_insert_sort(nums):
    """二分插入排序

    :param nums: list
        待排数组
    """
    def _binary_search(search_len):
        """通过二分查找找出数在前面的数组中的位置

        :param search_len: int
            要查找的数组的长度（不包含要查找的数）
        :return: int
            数组中的位置
        """
        # 得到要查找的数
        x = nums[search_len]
        left, right = 0, search_len - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < x:
                mid += 1