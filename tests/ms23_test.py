import unittest

from main.question23 import my1, book1


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.nums = list(range(10))
        self.head = my1.create_linklist(self.nums)

    def test_my1_create_linklist(self):
        self.assertEqual(self.nums, my1.display_linklist(self.head))

    def test_my1_first_node_ring(self):
        # 无环的情况
        self.assertEqual(None, my1.first_node_ring(self.head))

        # 有环的情况
        # 构建环
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        tail_node = current_node
        tail_node.next = self.head.next.next

        self.assertEqual(self.head.next.next, my1.first_node_ring(self.head))

        # 边界测试
        # 头节点为空
        self.assertEqual(None, my1.first_node_ring(None))

    def test_book1_first_ring_node(self):
        # 无环的情况
        self.assertEqual(None, book1.first_ring_node(self.head))

        # 有环的情况
        # 构建环
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        tail_node = current_node
        tail_node.next = self.head.next.next

        self.assertEqual(self.head.next.next, book1.first_ring_node(self.head))

        # 边界测试
        # 头节点为空
        self.assertEqual(None, book1.first_ring_node(None))


if __name__ == '__main__':
    unittest.main()
