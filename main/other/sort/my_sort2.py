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
        current_num = nums[search_len]

        left, right = 0, search_len - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < current_num:
                left = mid + 1
            else:
                right = mid - 1

        return left

    for i in range(1, len(nums)):
        x = nums[i]

        index = _binary_search(i)
        j = i
        while j > index:
            nums[j] = nums[j - 1]
            j -= 1

        nums[index] = x


def shell_sort(nums):
    """希尔排序

    :param nums: list
        待排数组
    """
    def _insert_sort(_nums, start_index, interval):
        """直接插入排序

        :param _nums: list
            待排数组
        :param start_index: int
            起始index
        :param interval:
            希尔排序的间隔
        """
        for i in range(start_index + interval, len(_nums), interval):
            x = _nums[i]

            j = i - interval
            while j >= start_index:
                if x >= _nums[j]:
                    break
                _nums[j + interval] = _nums[j]
                j = j - interval
            _nums[j + interval] = x

    for interval in range(len(nums) // 2, 0, -1):
        for start_index in range(interval):
            _insert_sort(_nums=nums, start_index=start_index, interval=interval)

################################################################################
#    选择排序
################################################################################
