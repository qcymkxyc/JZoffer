#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-20 上午11:08
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

书上考虑了大数情况,用字符串模拟加法，防止溢出
    
"""


def delete_zero(nums, n):
    """去除前面的零

    :param nums: list
        打印的数
    :param n: int
        n位数
    """
    for i, num in enumerate(nums):
        for digit in range(n):
            if num[digit] != "0":
                temp = num[digit:]
                nums[i] = temp
                break


def order_display(n):
    """顺序打印n位数

    :param n: int
        n位数
    :return : list
        打印结果
    """
    nums = ["0" * (n - 1) + "1"]
    # 生成数字
    while not increment(nums, n):
        pass
    # 删除前面的0
    delete_zero(nums, n)

    return nums


def increment(nums, n):
    """根据输入位数输出生成的n位数字（顺序排列）

    :param nums: list
        保存打印数字的list
    :param n: int
        位数
    :return: book
        是否溢出
    """
    last_num = nums[-1]

    temp = last_num
    for digit in range(n-1, -1, -1):
        last_ch = temp[digit]

        # 进位情况
        if last_ch == "9":
            temp = temp[:digit] + "0" + temp[digit + 1:]
        # 非进位
        else:
            current_ch = chr(ord(last_ch) + 1)
            current_num = temp[:digit] + current_ch + temp[digit + 1:]
            nums.append(current_num)
            return False

    return True
