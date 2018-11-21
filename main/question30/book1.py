#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:54
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

"""
from main.question30 import my1


class Stack(my1.Stack):
    def __init__(self):
        my1.Stack.__init__(self)
        self.assist_stack = list()

    def min(self):
        """返回最小值

        :return: int
        :raises:
            IndexError 栈为空
        """
        return self.assist_stack[-1]

    def push(self, value):
        my1.Stack.push(self, value)
        try:
            min_value = self.min()
        except IndexError:
            min_value = value
        else:
            if value < min_value:
                min_value = value
        finally:
            self.assist_stack.append(min_value)

    def pop(self):
        """
        :return: int
            弹出栈的值
        :raises:
            IndexError: 栈为空
        """
        pop_value = my1.Stack.pop(self)
        # 弹出辅助栈
        self.assist_stack.pop(-1)
        return pop_value

