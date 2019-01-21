#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-12 上午11:29
    @Author:  qcymkxyc
    @File: question1.py
    @Software: PyCharm

    有ｎ级台阶，一个人每次只能上一级或者两级，问有多少种走完台阶的方法
"""
ways = 0


def walk_way1(steps):
    """暴力搜索方法

    :param steps: int
        台阶数
    :return: int
        方法数
    """
    global ways
    ways = 0
    _inner_walk_ways1(steps)

    return ways


def _inner_walk_ways1(steps, walked=0):
    """暴力搜索方式

    :param steps: int
        台阶数
    """
    global ways
    if walked == steps:
        ways += 1
    if walked > steps:
        return

    _inner_walk_ways1(steps, walked + 1)
    _inner_walk_ways1(steps, walked + 2)


def walk_way2(steps):
    """动态规划

    :param steps: int
        台阶数
    :return: int
        方法数
    """
    ways_dict = dict()

    ways_dict[1] = 1
    ways_dict[2] = 2

    for s in range(3, steps + 1):
        w = ways_dict[s - 1] + ways_dict[s - 2]
        ways_dict[s] = w

    return ways_dict[steps]

