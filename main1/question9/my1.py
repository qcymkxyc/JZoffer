#!usr/bin/env python 
# -*- coding:utf-8 _*-  
""" 
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: my1.py
 @time: 2019/2/2 15:02
 
"""
class Stack:
    def __init__(self):
        self.core = list()

    def pop(self):
        return self.core.pop(-1)

    def push(self,val):
        self.core.append(val)

    def __len__(self):
        return len(self.core)

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def append_tail(self,val):
        """入队 """
        pass

    def delete_head(self):
        """出队"""
        pass

    def __len__(self):
        return len(self.stack1) + len(self.stack2)
