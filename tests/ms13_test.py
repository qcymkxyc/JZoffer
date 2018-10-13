import unittest

from main.question13 import my1


class MSTest(unittest.TestCase):

    def setUp(self):
        row, col = 10, 10
        self.matrix = (row, col)

    def test_edge_check(self):
        """边界检测"""
        # 小于0
        self.assertFalse(my1.edge_check(self.matrix, (-1, 0)))
        self.assertFalse(my1.edge_check(self.matrix, (0, -2)))
        self.assertFalse(my1.edge_check(self.matrix, (-12, -3)))

        # 超过行或列
        self.assertFalse(my1.edge_check(self.matrix, (12, 3)))
        self.assertFalse(my1.edge_check(self.matrix, (1, 13)))
        self.assertFalse(my1.edge_check(self.matrix, (12, 13)))

        # 正常情况
        self.assertTrue(my1.edge_check(self.matrix, (2, 3)))

    def test_num_check(self):
        """数位检测"""
        # 不超过情况
        self.assertTrue(my1.num_check((35, 37), 18))
        # 超过情况
        self.assertFalse(my1.num_check((35, 38), 18))

    def test_matrix_search(self):
        """搜索格子"""
        # 功能测试
        self.assertEqual(my1.matrix_search((2, 2), (0, 0), k=1), 3)
        # k为负数的情况
        self.assertEqual(my1.matrix_search(self.matrix, (0, 0), k=-1), 0)
        # k为0
        self.assertEqual(my1.matrix_search(self.matrix, (0, 0), k=0), 1)
        # 一行或一列的情况
        self.assertEqual(my1.matrix_search((1, 3), (0, 0), k=1), 2)
        self.assertEqual(my1.matrix_search((3, 1), (0, 0), k=1), 2)


if __name__ == '__main__':
    unittest.main()
