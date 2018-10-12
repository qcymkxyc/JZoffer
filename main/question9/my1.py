#!/usr/bin/python3
# coding=utf-8
"""

 @Time    : 18-9-27 上午10:41
 @Author  : qcymkxyc
 @Email   : qcymkxyc@163.com
 @File    : my1.py
 @Software: PyCharm
    
"""



class Stack:
    """
        栈
        Attributions:
            core : list
                用来存储元素
    """
    def __init__(self):
        self.core = list()

    def push(self,element):
        self.core.append(element)

    def pop(self):
        if len(self.core) == 0:
            raise IndexError("栈已空！")
        return  self.core.pop(-1)

    def clear(self):
        self.core.clear()

    def __len__(self):
        return len(self.core)


class Queue:
    """
        用两个栈实现的队列

    """
    stack1 = Stack()
    stack2 = Stack()

    def push(self,element):
        stack = self.stack1 if len(self.stack1) != 0 else self.stack2
        stack.push(element)


    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            raise IndexError("队列已空!")

        stack = self.stack1 if len(self.stack1) != 0 else self.stack2
        empty_stack = self.stack1 if stack != self.stack1 else self.stack2

        while len(stack) != 0:
            empty_stack.push(stack.pop())
        return empty_stack.pop()


    def clear(self):
        self.stack1.clear()
        self.stack2.clear()

    def __len__(self):
        stack = self.stack1 if len(self.stack1) != 0 else self.stack2
        return len(stack)

