#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-23 上午10:47
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""
count = 0


def translate(num):
    global count
    count = 0
    _translate(str(num), 0)
    return count


def _translate(s_num, i):
    global count
    if i == len(s_num) - 1:
        count += 1
        return
    if i >= len(s_num):
        return

    # 占一位
    _translate(s_num, i + 1)

    # 占两位
    sub_num = int(s_num[i: i + 2])
    if sub_num > 25:
        return
    else:
        _translate(s_num, i + 2)
