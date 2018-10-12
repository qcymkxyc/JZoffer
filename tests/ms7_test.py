import unittest

from main.question7 import my1

class MSTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_create_tree1(self):
        """
        测试不完全二叉树
        """
        front_ergodic = [1,2,4,7,3,5,6,8]
        mid_ergodic = [4,7,2,1,5,3,8,6]
        head = my1.create_tree(front_ergodic=front_ergodic,mid_ergodic=mid_ergodic)
        front_display_list = my1.front_display(head)
        self.assertEqual(front_ergodic,front_display_list)

    def test_create_tree2(self):
        """
        测试完全二叉树
        :return:
        """
        front_ergodic = [1,2,4,8,9,5,3,6,7]
        mid_ergodic = [8,4,9,2,5,1,6,3,7]
        head = my1.create_tree(front_ergodic,mid_ergodic)
        front_display_list = my1.front_display(head)
        self.assertEqual(front_ergodic,front_display_list)

    def test_create_tree3(self):
        """
            测试仅有左节点的树
        """
        front_ergodic = [1,2,3,4,5]
        mid_ergodic = [5,4,3,2,1]

        head = my1.create_tree(front_ergodic,mid_ergodic)
        front_display_list = my1.front_display(head)
        self.assertEqual(front_ergodic,front_display_list)

    def test_create_tree4(self):
        """
            测试仅有右节点的树
        """
        front_ergodic = [1,2,3,4,5]
        mid_ergodic = [1, 2, 3, 4, 5]

        head = my1.create_tree(front_ergodic,mid_ergodic)
        front_display_list = my1.front_display(head)
        self.assertEqual(front_ergodic,front_display_list)

    def test_create_tree5(self):
        """
            测试仅有一个节点
        """
        front_ergodic = [1]
        mid_ergodic = [1]

        head = my1.create_tree(front_ergodic,mid_ergodic)
        front_display_list = my1.front_display(head)
        self.assertEqual(front_ergodic,front_display_list)

    def test_create_tree6(self):
        """
            测试序列不匹配
        """
        front_ergodic = [1,2]
        mid_ergodic = [1,2,3]
        with self.assertRaises(IndexError):
            my1.create_tree(front_ergodic, mid_ergodic)


        front_ergodic = [1,2,3]
        mid_ergodic = [3,2,1]
        with self.assertRaises(LookupError):
            my1.create_tree(front_ergodic,mid_ergodic)
