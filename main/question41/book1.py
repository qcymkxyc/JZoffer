#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-6 上午9:35
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""
from operator import lt, gt


def _shift(nums, i, end, mode="max"):
    """堆的交换

    :param nums: List[int]
        数组
    :param i: int
        当前数的索引
    :param end: int
        交换的范围
    :param mode: str
        最大堆和最小堆的模式
    :return bool
        是否交换
    """
    sign = gt if mode == "max" else lt
    left_index = i * 2 + 1
    right_index = i * 2 + 2

    # 找出子节点的最大值
    if left_index >= end:  # 左节点超出范围
        return False
    elif right_index >= end:  # 右节点超出范围
        max_child_index = left_index
    else:
        max_child_index = left_index if sign(
            nums[left_index], nums[right_index]) else right_index

    # 交换
    if sign(nums[i], nums[max_child_index]):
        return False
    nums[i], nums[max_child_index] = nums[max_child_index], nums[i]

    return True


def _build_heap(nums, end, mode):
    """生成堆

    :param nums: List[int]
        数组
    :param end: int
        范围
    :param mode: str
        最大堆和最小堆的模式
    """
    i = end - 1
    while i >= 0:
        if _shift(nums, i, end, mode):
            i = 2 * i + 2
        i -= 1


def heap_sort(nums, mode="max"):
    """堆排序

    :param nums: List[int]
        数组
    :param mode: str
        模式
    """
    for end in range(len(nums), 1, - 1):
        _build_heap(nums, end, mode)
        nums[0], nums[end - 1] = nums[end - 1], nums[0]


class Median:
    """中位数"""

    def __init__(self):
        self.count = 0
        # 最大堆和最小堆
        self.max_heap = list()
        self.min_heap = list()

    def insert(self, num):
        self.count += 1
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            self.max_heap.append(num)
            return

        # 加入新数
        if num > self.max_heap[0]:
            self.min_heap.append(num)
        else:
            self.max_heap.append(num)
        _build_heap(self.max_heap, len(self.max_heap), "max")
        _build_heap(self.min_heap, len(self.min_heap), "min")

        # 当最大堆长度大于最小堆
        if len(self.max_heap) - len(self.min_heap) >= 2:
            max_num = self.max_heap.pop(0)
            self.min_heap.append(max_num)
            _build_heap(self.max_heap, len(self.max_heap), "max")
            _build_heap(self.min_heap, len(self.min_heap), "min")

        # 当最小堆长度大于最大堆
        if len(self.min_heap) - len(self.max_heap) >= 2:
            min_num = self.min_heap.pop(0)
            self.max_heap.append(min_num)
            _build_heap(self.max_heap, len(self.max_heap), "max")
            _build_heap(self.min_heap, len(self.min_heap), "min")

    def median(self):
        if self.count % 2 == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.max_heap[0] if len(
                self.max_heap) > len(
                self.min_heap) else self.min_heap[0]

    def __str__(self):
        return str(self.median())
