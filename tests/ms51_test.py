import unittest
from main.question51 import my1, book1


class MSTestCase(unittest.TestCase):
    def test_reverse_tuple(self):
        nums = [7, 5, 6, 4]
        self.assertEqual(5, my1.reverse_tuple(nums))

        self.assertEqual(0, my1.reverse_tuple([]))
        self.assertEqual(0, my1.reverse_tuple([1]))

    def test_book1_reverse_tuple(self):
        nums = [7,5,6,4]
        self.assertEqual(5, book1.reverse_tuple(nums)[1])

        self.assertEqual(0, book1.reverse_tuple([])[1])
        self.assertEqual(0, book1.reverse_tuple([1])[1])


if __name__ == '__main__':
    unittest.main()
