import unittest
from main1.question3 import my1, book1, my2, book2


class MSTestCase(unittest.TestCase):
    def test_my1_repeat_num(self):
        nums = [2, 3, 1, 0, 2, 5, 3]
        num = my1.repeat_num(nums)
        self.assertIn(num, [2, 3])

        self.assertEqual(None, my1.repeat_num(None))
        self.assertEqual(None, my1.repeat_num([1, 2, 3, 4, 5]))

    def test_book1_repeat_num(self):
        nums = [2, 3, 1, 0, 2, 5, 3]
        self.assertTrue(book1.repeat_num(nums))

        nums = [2, 3, 1, 2, 5, 3]
        self.assertTrue(book1.repeat_num(nums))
        self.assertFalse(book1.repeat_num([1, 2, 3, 4, 0]))

        with self.assertRaises(ValueError):
            book1.repeat_num([1, 2, 3, 4, 5])

    def test_my2_repeat_num(self):
        nums = [2, 3, 1, 0, 2, 5, 3]
        num = my2.repeat_num(nums)
        self.assertIn(num, [2, 3])

    def test_book2_repeat_num(self):
        nums = [2, 3, 1, 0, 2, 5, 3]
        num = book2.repeat_num(nums)
        self.assertIn(num, [2, 3])

        nums = [1,2,3,4,5]
        with self.assertRaises(ValueError):
            book2.repeat_num(nums)
            book2.repeat_num([])
            book2.repeat_num([1])


if __name__ == '__main__':
    unittest.main()
