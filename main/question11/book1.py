#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-7 上午11:20
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm
    
"""
def binary_find_min(nums):
    """利用二分查找寻找旋转数组的最小值

    :param nums: list
        旋转数组
    :return: int
        最小值
    :raises:
        TypeError:  旋转数组为空
    """
    def order_search(nums):
        """顺序查找

        :param nums: list
            旋转数组
        :return: int
            最小值
        """
        min_num = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
        return min_num

    if not nums:
        raise TypeError("旋转数组为空")

    left,right = 0,len(nums) - 1
    #旋转个数为0的情况
    if nums[left] < nums[right]:
        return nums[left]

    while left + 1 < right:
        mid = (left + right) // 2
        #边界情况
        if nums[left] == nums[mid] == nums[right]:
            return order_search(nums)

        if nums[mid] >= nums[left]:
            left = mid
        if nums[mid] < nums[right]:
            right = mid


    return nums[right]