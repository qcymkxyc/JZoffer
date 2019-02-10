#!usr/bin/env python 
# -*- coding:utf-8 _*-  
""" 
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: my1.py
 @time: 2019/2/10 11:06
 
"""


def reverse_sentence(sentence):
    """翻转句子

    :param sentence: str
        句子
    :return: str
        翻转后的句子
    """
    words = sentence.split()
    stack = list()
    for i, w in enumerate(words):
        stack.append(w)

    temp = []
    while len(stack) > 0:
        temp.append(stack.pop(-1))

    return " ".join(temp)
