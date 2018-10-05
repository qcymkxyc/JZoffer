#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-30 上午11:49
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book_sort.py
@Software: PyCharm

书上的排序算法实现
    
"""
import copy

def quick_sort(nums,start = 0,end = None):
    """
        快速排序

    :param nums: list or tuple
        要排序的数组
    """
    def partition(nums,start,end):
        left = start
        right = end
        x = nums[left]
        while(left < right):
            while(left < right):
                if nums[right] < x:
                    nums[left] = nums[right]
                    break
                right -= 1

            while(left < right):
                if nums[left] > x:
                    nums[right] = nums[left]
                    break
                left += 1
        nums[left] = x
        return left

    if start == end:
        return
    if not end:
        end = len(nums) - 1

    index = partition(nums,start,end)

    if index > start:
        quick_sort(nums,start,index - 1)
    if index < end:
        quick_sort(nums,index + 1,end)


def heap_sort(nums):
    """堆排序

    :param nums: list
        待排序数组
    :return: list
        排序后的数组
    """
    def heapify(nums,i,n):
        """构造堆

        :param nums: list
            构造数组
        :param i: int
            构造堆的根节点的index
        :param n: int
            构造堆的尾结点的限制，即节点的index不得超过n
        """
        x = nums[i]
        left_child_index = i * 2

        #当i是非叶子节点时
        while(left_child_index <= n):
            #确定最大子树
            if i * 2 + 1 <= n and nums[i * 2 + 1] > nums[left_child_index]:
                max_child_index = i * 2 + 1
            else:
                max_child_index = left_child_index

            if x > nums[max_child_index]:
                return
            else:
                nums[i],nums[max_child_index] = nums[max_child_index],x
                i = max_child_index
                left_child_index = i * 2

    temp = copy.copy(nums)
    temp.insert(0,None)
    n = len(nums)
    for i in range(n // 2,0,-1):
        heapify(temp,i,n)

    for i in range(n,1,-1):
        temp[i],temp[1] = temp[1],temp[i]
        heapify(temp,1,i - 1)

    return temp[1:]





