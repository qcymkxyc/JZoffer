import unittest

from main.question18 import my1, my2


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.data = list(range(1, 10))
        self.head = my1.create_list(self.data)

    def test_my1_create_list(self):
        data = [1, 2, 3]
        head = my1.create_list(data)

        current_node = head
        for i, value in enumerate(data):
            self.assertEqual(value, current_node.value)
            current_node = current_node.next

    def test_my1_delete_node(self):
        # 准备要删除的结点
        delete_node_index = 3
        delete_node = None
        current_node = self.head
        for i in range(len(self.data)):
            current_node = current_node.next
            if i == delete_node_index:
                delete_node = current_node
                break

        # 功能测试
        my1.delete_node(self.head, delete_node)
        current_node = self.head
        while current_node:
            self.assertNotEqual(current_node, delete_node)
            self.assertNotEqual(current_node.value, delete_node.value)
            current_node = current_node.next

        # 边界测试
        # 删除的结点是head的情况
        my1.delete_node(self.head, self.head)
        self.assertNotEqual(0, self.head.value)

        with self.assertRaises(TypeError):
            my1.delete_node([1, 2, 3], delete_node)

        with self.assertRaises(ValueError):
            my1.delete_node(self.head, delete_node)

    def test_my2_delete_duplication(self):
        data = (1, 2, 2, 3, 3, 4, 5)
        head = my1.create_list(data)
        # 有序的数据
        order_data = sorted(list(set(data)))

        # 功能测试
        my2.delete_duplication(head)
        current_node = head
        for i, val in enumerate(order_data):
            self.assertEqual(val, current_node.value)
            current_node = current_node.next


if __name__ == '__main__':
    unittest.main()
