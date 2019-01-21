#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-16 上午11:38
    @Author:  qcymkxyc
    @File: my2.py
    @Software: PyCharm

    本题扩展
"""
import copy


def all_combination(s):
    """字符串的所有组合

    :param s: str
        字符串
    :return: List[str]
        所有组合的list
    """
    def _combination(pre_index,comb):
        """迭代用

        :param pre_index: List[int]
            之前用过的索引
        :param comb: List[str]
            用来保存所有可能
        """
        for i in range(len(s)):
            if i in pre_index:
                continue
            temp_index = copy.copy(pre_index)
            temp_index.append(i)
            comb.append("".join([s[j] for j in temp_index]))
            _combination(temp_index,comb)

    comb = list()
    _combination(pre_index=[],comb = comb)

    # 去重
    comb = ["".join(sorted(sub_s)) for sub_s in comb]
    comb = list(set(comb))
    return comb
