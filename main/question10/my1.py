#!/usr/bin/python3
# coding=utf-8
"""

 @Time    : 18-9-28 上午11:51
 @Author  : qcymkxyc
 @Email   : qcymkxyc@163.com
 @File    : my1.py
 @Software: PyCharm

 对本节的一点理解：虽然本节是对斐波纳契的应用，但感觉背后的逻辑是对动态规划的
 使用，比如题目二及其相关题目，更确切的说是动态规划。对于动态规划的实用范围有两点：

 1. 某一步的可能性明确，即在这一步有多少种可能的选择必须明确
 2. 后续步骤和当前步骤无关

"""

def fibonacci(n):
    """求第n个斐波那切数
    :param n:int
        个数index
    :return:int
        第n个斐波纳契数 
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

