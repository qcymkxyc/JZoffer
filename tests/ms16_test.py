import unittest

from main.question16 import my1, book1, book2


class MSTest(unittest.TestCase):

    def test_my1_power(self):
        # 正数测试
        self.assertEqual(my1.power(2, 5), 32)

        # 负数测试
        self.assertEqual(my1.power(2, -5), 1/32)

        # 0测试
        self.assertEqual(my1.power(2, 0), 1)

    def test_book1_power(self):
        self.assertEqual(book1.power(2, 5), 32)
        self.assertEqual(book1.power(2, -5), 1/32)

        with self.assertRaises(ZeroDivisionError):
            book1.power(0, -1)
        self.assertEqual(book1.power(2, 0), 1)

    def test_book2_power(self):
        # 正数范围
        # 奇数
        self.assertEqual(book2.power(2, 5), 32)
        # 偶数
        self.assertEqual(book2.power(2, 4), 16)

        # 负数范围
        # 奇数
        self.assertEqual(book2.power(2, -5), 1/32)
        # 偶数
        self.assertEqual(book2.power(2, -4), 1/16)

        # 0
        with self.assertRaises(ZeroDivisionError):
            book2.power(0, -1)
        self.assertEqual(book2.power(2, 0), 1)


if __name__ == '__main__':
    unittest.main()
