#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-27 上午10:58
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""


def longest_substr(s):
    """最长子字符串

    动态规划
    :param s: str
        母字符串
    :return: int
        最长子字符串长度
    """
    if len(s) == 0:
        return 0

    longest_dict = dict()
    longest_dict[0] = 1
    for i, ch in enumerate(s):
        if i == 0:
            continue

        pre_s = s[:i]
        # 有重复
        if ch in pre_s:
            distance = i - pre_s.rindex(ch)
            if distance > longest_dict[i - 1]:
                longest_dict[i] = longest_dict[i - 1] + 1
            else:
                longest_dict[i] = longest_dict[i - 1]
        # 无重复
        else:
            longest_dict[i] = longest_dict[i - 1] + 1

    return longest_dict[len(s) - 1]
