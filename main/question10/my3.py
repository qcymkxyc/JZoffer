#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-29 下午1:25
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my3.py
@Software: PyCharm

题目二的扩展题目
    
"""

def jump(n):
    """跳台阶的扩展题目

    同样将问题看成动态规划，对于台阶数n，目前而言有n种选择方式,即从1到n，
    在函数实现中，对这n种方式累加，最后得到台阶数为n的方式个数

    :param n: int
        台阶的个数
    :return: int
        跳法的种数
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    sum = 0
    for i in range(1,n):
        sum += jump(i)
    return sum + 1
