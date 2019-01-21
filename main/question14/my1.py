#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-15 上午10:47
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

    个人理解动态规划适用于问题的分解，而贪婪算法适用于问题的合并。即动态规划通常用于
    自上而下问题的拆分，然后将子问题拼凑而成；贪婪算法适用于自下而上的最好情况尝试。

"""


def compute_max_mul(rope_len):
    """计算绳子的最大乘积

    异常情况：
        rope_len小于等于0
    正常情况：
        迭代停止条件：绳子长度为1
        分子绳子分为以下两种情况：
            1. 其中一段子绳子为0，即不分为两段
            2. 两段子绳子均不为0

    :param rope_len: int
        绳子长度
    :return: int
        最大乘积
    :raises:
        ValueError: 绳子长度错误
    """
    if rope_len <=0:
        raise ValueError("绳子长度错误！")

    if rope_len == 1:
        return 1

    # 不分为两段的情况
    current_muls = [rope_len]   # 当前的子绳子的所有乘积
    # 分成左右两段
    for i in range(1, rope_len):
        sub_rope_len1 = i
        sub_rope_len2 = rope_len - i
        current_muls.append(compute_max_mul(sub_rope_len1) * compute_max_mul(sub_rope_len2))

    return max(current_muls)
