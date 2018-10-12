
"""
    通过栈实现倒序打印
"""
class Node(object):
    data = None
    next_node = None

def create_ListNode(count = 10):
    """
    创建链表
    :param count:元素个数
    :return:
    """
    front = None
    for i in range(count):
        node = Node()
        node.data = i
        if front is None:
            front = node
            head = front
            continue
        front.next_node = node
        front = node
    return head

def display_ListNode(head):
    node = head
    while node != None:
        print(node.data)
        node = node.next_node

class Stack(object):
    core = list()
    def push(self,num):
        self.core.append(num)
    def pop(self):
        if len(self.core) != 0:
            return self.core.pop(-1)
        return None
    def clear(self):
        self.core.clear()
    def __len__(self):
        return len(self.core)

def push_in_stack(list_node_head,stack):
    """
    压入栈中
    :param list_node_head:Node
        链表的head
    :param stack:Stack
        栈
    :return:
    """
    node = list_node_head
    while node != None:
        stack.push(node.data)
        node = node.next_node
