import unittest

from main.question25 import my1
from main.question23 import my1 as q23


class MSTestCase(unittest.TestCase):
    def setUp(self):
        data1 = list(filter(lambda x: x % 2 == 1, range(10)))
        data2 = list(filter(lambda x: x % 2 == 0, range(10)))

        self.link1 = q23.create_linklist(data1)
        self.link2 = q23.create_linklist(data2)

    def test_links(self):
        """测试输入数据"""
        self.assertEqual([1, 3, 5, 7, 9], q23.display_linklist(self.link1))
        self.assertEqual([0, 2, 4, 6, 8], q23.display_linklist(self.link2))

    def test_my1_merge_linklist(self):
        # 一般情况
        # [1, 3, 5, 7, 9] 和 [0, 2, 4, 6, 8]
        merge_head = my1.merge_linklist(self.link1, self.link2)
        self.assertEqual(list(range(10)), q23.display_linklist(merge_head))

        # 不需要穿插的情况
        # [1,2,3] 和[4,5,6]
        link1 = q23.create_linklist([1, 2, 3])
        link2 = q23.create_linklist([4, 5, 6])
        merge_head = my1.merge_linklist(link1, link2)
        self.assertEqual(list(range(1, 7)), q23.display_linklist(merge_head))

        # 中间有几个相同的情况
        link1 = q23.create_linklist([1, 2, 3, 6])
        link2 = q23.create_linklist([2, 5, 6])
        merge_head = my1.merge_linklist(link1, link2)
        self.assertEqual([1, 2, 2, 3, 5, 6, 6], q23.display_linklist(merge_head))

        # 相同的情况
        link1 = q23.create_linklist([1, 1, 1])
        link2 = q23.create_linklist([1, 1, 1])
        merge_head = my1.merge_linklist(link1, link2)
        self.assertEqual([1] * 6, q23.display_linklist(merge_head))

        #  其中一个为空链表的情况
        link1 = q23.create_linklist([])
        link2 = q23.create_linklist([4, 5, 6])
        merge_head = my1.merge_linklist(link1, link2)
        self.assertEqual([4, 5, 6], q23.display_linklist(merge_head))

        # 两个空链表
        link1 = q23.create_linklist([])
        link2 = q23.create_linklist([])
        merge_head = my1.merge_linklist(link1, link2)
        self.assertEqual([], q23.display_linklist(merge_head))


if __name__ == '__main__':
    unittest.main()
