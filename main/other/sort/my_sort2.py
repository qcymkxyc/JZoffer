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
            _insert_sort(
                _nums=nums,
                start_index=start_index,
                interval=interval)

##########################################################################
#    选择排序
##########################################################################


def select_sort(nums):
    """简单选择排序

    :param nums: list
        待排数组
    """
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[min_index], nums[i] = nums[i], nums[min_index]

# TODO 堆排序

##########################################################################
#   交换排序
##########################################################################


def bubble_sort(nums):
    """冒泡排序

    :param nums: list
        待排数组
    """
    for i in range(len(nums)):
        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


def quick_sort(nums, left, right):
    """快速排序

    :param nums: list
        待排数组
    """
    def inner_sort(inner_nums, start=0, end=len(nums) - 1):
        """快速排序的交换部分

        :param inner_nums: list
            待排数组
        :param start: int
            开始的index
        :param end: int
            结束的index
        """
        if start >= end:
            return -1

        inner_left, inner_right = start, end
        base = inner_nums[start]
        while inner_left < inner_right:
            # right从右向左走
            while True:
                if inner_left >= inner_right:
                    break
                num = inner_nums[inner_right]
                if num < base:
                    inner_nums[inner_left] = num
                    break
                inner_right -= 1

            # left从左向右走
            while True:
                if inner_left >= inner_right:
                    break
                num = inner_nums[inner_left]
                if num > base:
                    inner_nums[inner_right] = num
                    break
                inner_left += 1

        inner_nums[inner_left] = base
        return inner_left

    position = inner_sort(nums, left, right)
    # num = nums[position]
    # 当数组中仅有一个数或者没有数时则不作任何行为
    if position == -1:
        return

    quick_sort(nums, left, position)
    quick_sort(nums, position + 1, right)
