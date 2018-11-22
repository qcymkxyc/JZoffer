#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:29
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

"""


def is_pop_seq(push_seq, pop_seq):
    """判断此出栈顺序是不是出栈顺序

    :param push_seq: list
        入栈顺序
    :param pop_seq: list
        要衡量的出栈顺序
    :return: bool
        是否是出栈顺序的一种
    :raises:
        ValueError : 出入栈个数不匹配
    """
    if len(push_seq) != len(pop_seq):
        raise ValueError("个数不匹配")
    if set(push_seq) != set(pop_seq):
        raise ValueError("元素不匹配")
    if (not push_seq) or (not pop_seq):
        raise ValueError("序列不能为空")

    stack = list()  # 辅助栈
    while not (len(stack) == 0 and len(push_seq) == 0):
        try:
            stack_pop_v = stack[-1]
        # 最开始的情况，即辅助栈为空时
        except IndexError:
            stack.append(push_seq.pop(0))
        else:
            # 辅助栈和出栈第一个元素相同，则出栈
            if stack_pop_v == pop_seq[0]:
                stack.pop(-1)
                pop_seq.pop(0)
            # 不相同的情况，入栈
            else:
                try:
                    stack.append(push_seq.pop(0))
                # 入栈序列空了且也不相同则返回False
                except IndexError:
                    return False
    return True
