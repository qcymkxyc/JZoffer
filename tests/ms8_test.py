import unittest

from main.question8 import my1


class MSTest(unittest.TestCase):


    def setUp(self):
        self.front = [1,2,4,7,3,5,6,8]
        self.mid = [4,7,2,1,5,3,8,6]
        self.current_node = None
        self.head = my1.create_tree(self.front,self.mid)


    def tearDown(self):
        pass

    def test_create_tree(self):
        """
            创建树测试
        """
        front = [1,2,4,7,3,5,6,8]
        mid = [4,7,2,1,5,3,8,6]

        head = my1.create_tree(front,mid)
        front_display = my1.front_display(head)
        self.assertEqual(front,front_display)

    def find_current_node(self,head,data):
        """
            找出树的对应的data的节点
        :param head: TreeNode
            树的根节点
        :param data:数据
        :return: TreeNode
            data对应的节点
        """
        if not head:
            return

        #已经找到当前节点的情况
        if self.current_node:
            return

        if head.data == data:
            self.current_node = head

        self.find_current_node(head.left_child,data)
        self.find_current_node(head.right_child,data)

    def test_find_node(self):
        """
            测试找到节点
        """
        head = my1.create_tree(self.front,self.mid)
        self.find_current_node(head,5)
        self.assertEqual(3,self.current_node.parent.data)
        self.assertEqual(self.current_node.data,5)

    def test_mid_next1(self):
        """
            测试左叶子节点
        """
        self.current_node = None
        head = my1.create_tree(self.front,self.mid)
        self.find_current_node(head,5)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(3,next_node.data)

        self.current_node = None
        self.find_current_node(head,8)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(6,next_node.data)

    def test_mid_next2(self):
        """
            测试右叶子节点
        """
        self.find_current_node(self.head,7)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(2,next_node.data)

    def test_mid_next3(self):
        """
            仅有左子树的非叶子节点
        """
        self.find_current_node(self.head,2)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(1,next_node.data)

    def test_mid_next4(self):
        """
            仅有右子树的非叶子节点
        """
        self.find_current_node(self.head,4)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(7,next_node.data)

    def test_mid_next5(self):
        """
            左右均有
        """
        self.find_current_node(self.head,1)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(5,next_node.data)

        self.current_node = None
        self.find_current_node(self.head,3)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(8,next_node.data)

    def test_mid_next6(self):
        """
            最后一个节点
        """
        self.find_current_node(self.head,6)
        next_node = my1.find_mid_next(self.current_node)
        self.assertEqual(None,next_node)