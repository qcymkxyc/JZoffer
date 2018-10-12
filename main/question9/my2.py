#!/usr/bin/python3
# coding=utf-8
"""

 @Time    : 18-9-28 上午10:58
 @Author  : qcymkxyc
 @Email   : qcymkxyc@163.com
 @File    : my2.py
 @Software: PyCharm

 相关题目: 两个队列实现一个栈

"""

class Queue:
    """队列"""

    def __init__(self):
        self.__core = list()

    def pop(self):
        """

        :return: object
        :raises:
            IndexError：队列为空
        """
        if len(self.__core) == 0:
            raise IndexError("队列已为空")
        return self.__core.pop(0)

    def push(self,element):
        self.__core.append(element)

    def __len__(self):
        return len(self.__core)

class Stack:
    """用两个队列实现的栈"""

    def __init__(self):
        self.__queues = (Queue(),Queue())

    def push(self,element):
        """入队
        :param element: object
            入队元素
        """
        queue1 = self.__queues[0]
        queue2 = self.__queues[1]

        use_queue = queue1 if len(queue1) != 0 else queue2
        use_queue.push(element)

    def pop(self):
        """
        :return object
            出队的元素
        :raise
            IndexError :栈为空
        """
        if len(self.__queues[0]) == 0 and len(self.__queues[1]) == 0:
            raise IndexError("栈已为空！")

        use_queue = self.__queues[0] if len(self.__queues[0])!= 0 else self.__queues[1]
        other_queue = self.__queues[0] if use_queue != self.__queues[0] else self.__queues[1]

        while len(use_queue) > 1:
            other_queue.push(use_queue.pop())

        return use_queue.pop()

