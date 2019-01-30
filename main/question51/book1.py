#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-30 上午10:49
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""


def _merge(nums1, nums2):
    """合并两个数组

    :param nums1:   List[int]
        数组一
    :param nums2:   List[int]
        数组二
    :return: List[int], int
        合并数组, 反转统计
    """
    merge_num = list()
    reverse_count = 0
    while len(nums1) != 0 and len(nums2) != 0:
        if nums1[-1] > nums2[-1]:
            reverse_count += len(nums2)
            merge_num.insert(0, nums1.pop(-1))
            # merge_num.append(nums1.pop(-1))
        else:
            # merge_num.append(nums2.pop(-1))
            merge_num.insert(0, nums2.pop(-1))

    merge_num = nums1 + merge_num
    merge_num = nums2 + merge_num

    return merge_num, reverse_count


def reverse_tuple(nums):
    """逆序对

    :param nums: List[int]
        数组
    :return: List[int],int
        排序序列,逆序对的个数
    """
    if len(nums) == 0:
        return nums, 0
    if len(nums) == 1:
        return nums, 0

    middle = len(nums) // 2
    left_nums = nums[:middle]
    right_nums = nums[middle:]

    left_nums, left_reverse = reverse_tuple(left_nums)
    right_nums, right_reverse = reverse_tuple(right_nums)
    merge_nums, reverse_count = _merge(left_nums, right_nums)

    return merge_nums, reverse_count + left_reverse + right_reverse
