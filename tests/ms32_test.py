import unittest
from main.question32 import book1, my2
from main.question26 import my1 as q26
import numpy as np


class MSTestCase(unittest.TestCase):
    def setUp(self):
        self.pre_order = [8, 6, 5, 7, 10, 9, 11]
        self.in_order = [5, 6, 7, 8, 9, 10, 11]

        self.root = q26.create_binary_tree(self.pre_order, self.in_order)

    def test_book1_level_display(self):
        # 功能测试
        self.assertEqual([8, 6, 10, 5, 7, 9, 11], book1.level_display(self.root))

        # 仅有左子树
        pre_order = [1, 2, 3, 4, 5]
        in_order = [5, 4, 3, 2, 1]
        root = q26.create_binary_tree(pre_order, in_order)
        self.assertEqual([1, 2, 3, 4, 5], book1.level_display(root))

        # 仅有右子树
        pre_order = [1, 2, 3, 4, 5]
        in_order = [1, 2, 3, 4, 5]
        root = q26.create_binary_tree(pre_order, in_order)
        self.assertEqual([1, 2, 3, 4, 5], book1.level_display(root))

        # 根结点为空
        self.assertEqual([], book1.level_display(None))

    def test_my2_breadth_first_search(self):
        """测试图的广度遍历(邻接矩阵)"""
        adjacency_matrix = np.asarray([
            [0, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0]
        ])
        self.assertEqual([0, 3, 1, 2], my2.breadth_first_search(adjacency_matrix))

        adjacency_matrix = np.asarray([
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1]
        ])
        self.assertEqual([0, 1, 3, 4], my2.breadth_first_search(adjacency_matrix))


if __name__ == '__main__':
    unittest.main()
