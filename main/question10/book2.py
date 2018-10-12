#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-29 下午12:13
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book2.py
@Software: PyCharm

题目二:青蛙跳台阶
    
"""

def jump(n):
    """求跳台阶的方式有多少种

    书上解析可以看成是一种动态规划的思想，即在当前情况下仅有两种选择：
    跳一步或两步，之后又重新开始,即后续的选择和现在无关

    :param n: int
        台阶的个数
    :return: int
        方式的个数
    """
    #保存跳台阶的方式个数，1和2表示跳一个和两个台阶的方式个数
    jump_list = [1,2]

    for i in range(3,n + 1):
        last_index = i - 2
        second_last_index = i - 3
        jump_num = jump_list[last_index] + jump_list[second_last_index]
        jump_list.append(jump_num)

    return jump_list[-1]