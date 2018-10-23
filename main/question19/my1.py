#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-22 上午11:49
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


# TODO  差* 规则
def asterisk_match(pattern, pattern_index, string, string_index):
    """

    :param pattern:
    :param pattern_index:
    :param string:
    :param string_index:
    :return:
    """
    pattern_last_ch = pattern[pattern_index - 1]
    try:
        pattern_next_ch = pattern[pattern_index + 1]
    except IndexError:
        pattern_next_ch = ""



def regex_match(patten, string):
    """正则表达式匹配

    两个匹配符号分别处理：
    1. .
    2. *

    :param patten: str
        匹配模式
    :param string: str
        匹配字符串
    :return: bool
        是否匹配
    """
    pattern_index = 0   # 模式的索引
    is_match = False    # 是否匹配

    for i, ch in enumerate(string):
        # 模式扫描完且均匹配的情况
        if pattern_index >= len(patten):
            break

        patten_ch = patten[pattern_index]   # 模式的字符串
        # 字符串和模式不相同的情况
        if patten_ch != ch:
            if patten_ch == ".":
                pass
            elif patten_ch == "*":
                # TODO * 规则
                pass
            else:   # 常规字符的情况
                pattern_index = 0
                continue

        pattern_index += 1

    # 模式扫描完且均匹配的情况
    if pattern_index >= len(patten):
        is_match = True

    return is_match
