#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-29 下午1:54
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book4.py
@Software: PyCharm

书上的相关题目
    
"""

def retangle_wag(n = 8):
    """小矩形放入大矩形的方式个数

    :param n:int
        小矩形的个数
    :return: int
        方式个数
    """
    #一个和两个小矩形的放入个数
    if n == 1:
        return 1
    if n == 2:
        return 2

    return retangle_wag(n - 1) + retangle_wag(n - 2)