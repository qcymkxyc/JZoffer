import unittest

from main.面试题3 import my1
from main.面试题3 import my2
from main.面试题3 import book1
from main.面试题3 import book2

class MSTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_my_find_same1(self):
        nums = [2,3,1,0,2,5,3]
        self.assertEqual(my1.find_same1(nums), [2, 3])

    def test_my_find_same2(self):
        nums = [2, 3, 1, 0, 2, 5, 3]
        self.assertEqual(my1.find_same2(nums),[2,3])

    def test_my_find_same3(self):
        """
            题目2
        """
        nums = [2,3,5,4,3,5,6,7]
        self.assertEqual([3,5],my2.find_same1(nums))

    def test_my_find_same4(self):
        """
            题目2
        """
        nums = [2, 3, 5, 4, 3, 5, 6, 7]
        self.assertEqual([3,5],my2.find_same2(nums))

    def test_book_find_same1(self):
        nums = [2, 3, 1, 0, 2, 5, 3]
        self.assertEqual([2,3],book1.find_same(nums))

    def test_book_find_same2(self):
        """
            题目2
        """
        nums = [2, 3, 1, 0, 2, 5, 3]
        self.assertTrue(book2.find_same(nums) in [2,3])

    def tearDown(self):
        pass