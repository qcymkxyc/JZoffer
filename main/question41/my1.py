#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-5 上午10:00
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


class Median:
    """中位数"""

    def __init__(self):
        self.core = list()

    def append(self, obj):
        self._insert_sort(obj)

    def _insert_sort(self, obj):
        self.core.append(obj)
        for i in range(len(self) - 2, -1, -1):
            if self.core[i] > obj:
                self.core[i + 1] = self.core[i]
            else:
                self.core[i + 1] = obj
                break

    def median_num(self):
        if len(self) % 2 == 0:
            median1 = self.core[int(len(self) / 2)]
            median2 = self.core[int(len(self) / 2) - 1]
            median = (median1 + median2) / 2
        else:
            median = self.core[len(self) // 2]
        return median

    def __len__(self):
        return len(self.core)

    def __str__(self):
        median = self.median_num()
        return str(median)

    def __repr__(self):
        return self.__str__()
