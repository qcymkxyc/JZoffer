#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-29 上午11:40
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

题目一书上的解法
    
"""
def fibonacci(n):
    """
    斐波纳契数列（从前往后循环求解）
    :param n:int
        第n个数
    :return: int
        斐波纳契数
    """
    #存储斐波纳契数的list
    fibonacci_list = [0,1]

    for i in range(2,n + 1):
        fibonacci_num = fibonacci_list[i - 1] + fibonacci_list[i - 2]
        fibonacci_list.append(fibonacci_num)

    return fibonacci_list[-1]


