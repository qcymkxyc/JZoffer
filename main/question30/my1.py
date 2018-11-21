#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:23
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

"""


class Stack:
    """栈

    利用一个min的index指针表示最小元素的index，即可
    实现O（1）

    """
    __slots__ = ("_core", "_min_index")

    def __init__(self):
        self._core = list()
        self._min_index = None

    def min(self):
        if len(self._core) == 0:
            raise ValueError("栈为空")
        return self._core[self._min_index]

    def push(self, value):
        # 首个元素
        if len(self._core) == 0:
            self._min_index = 0
        # 非首个元素
        else:
            if value < self.min():
                self._min_index = len(self._core)
        self._core.append(value)

    def pop(self):
        return self._core.pop(-1)
