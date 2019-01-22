#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-14 上午10:40
    @Author:  qcymkxyc
    @File: question4.py
    @Software: PyCharm

   假设有几种硬币，如1、3、5，并且数量无限。
   请找出能够组成某个数目的找零所使用最少的硬币数。
"""


def least_coin(num):
    """最少的硬币数

    :param num: int
        数
    :return: int
        硬币数
    """
    least_list = list()
    least_list.append(1)
    least_list.append(2)
    least_list.append(1)
    least_list.append(2)
    least_list.append(1)

    for n in range(6, num + 1):
        i = n - 1
        min_coin = min(least_list[i - 1],
                       least_list[i - 3],
                       least_list[i - 5]) + 1
        least_list.append(min_coin)

    # print(least_list)
    return least_list[-1]


"""扩展1
    一个矩形区域被划分为N*M个小矩形格子，在格子(i,j)中有A[i][j]个苹果。
    现在从左上角的格子(1,1)出发，要求每次只能向右走一步或向下走一步，最后到达(N,M)，
    每经过一个格子就把其中的苹果全部拿走。请找出能拿到最多苹果数的路线。
"""