#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-27 上午10:36
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def _is_repeate(s, start, end):
    """判断是否是重复的字符串

    :param s: str
        母字符串
    :param start: int
        开始位置
    :param end: int
        结束位置
    :return: bool
        是否不重复
    """
    sub_s = s[start:end]
    return len(sub_s) == len(set(sub_s))


def longest_substr(s):
    """最长子字符串

    暴力解法
    :param s: str
        母字符串
    :return: str
        最长子字符串
    """
    if len(s) == 0:
        return s

    windows_size = len(s)
    start = 0
    while windows_size >= 1:
        end = start + windows_size
        if end > len(s):
            windows_size -= 1
            start = 0

        else:
            # 如果子字符串没有重复的
            if _is_repeate(s, start, end):
                return s[start: end]

        start += 1

    return s[0]
