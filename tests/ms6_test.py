import unittest

from main.question6 import my1

class MSTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_create_list(self):
        head = my1.create_ListNode(10)
        my1.display_ListNode(head)

    def test_reverse_display(self):
        """
        倒序打印
        :return:
        """
        l = [i for i in range(9, -1, -1)]
        head = my1.create_ListNode()
        stack = my1.Stack()
        my1.push_in_stack(head, stack)
        r = []
        while len(stack) != 0:
            r.append(stack.pop())
        self.assertEqual(r,l,"结果错误")