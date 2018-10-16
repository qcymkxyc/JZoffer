import unittest

from main.question15 import my1, my2, book1, book2, my3, my4


class MyTest(unittest.TestCase):

    def test_my1_bin_count(self):
        self.assertEqual(my1.bin_count(9), 2)

    def test_my2_bin_count(self):
        self.assertEqual(my2.bin_count(9), 2)

    def test_book1_bin_count(self):
        self.assertEqual(book1.bin_count(9), 2)

    def test_book2_bin_count(self):
        self.assertEqual(book2.bin_count(9), 2)

############################################################
#   相关题目
#############################################################

    def test_my3_power2(self):
        self.assertEqual(my3.power_2(64), True)

        self.assertEqual(my3.power_2(13), False)

    def test_my4_transform_count(self):
        self.assertEqual(my4.transform_count(10, 13), 3)


if __name__ == '__main__':
    unittest.main()
