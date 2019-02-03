import unittest
from main1.question10 import my1,book1


class MSTestCase(unittest.TestCase):
    def test_my1_fibonacci(self):
        self.assertEqual(55, my1.fibonacci(10))

    def test_book1_fibonaci(self):
        self.assertEqual(3,book1.fibonacci(4))
        self.assertEqual(55, book1.fibonacci(10))


if __name__ == '__main__':
    unittest.main()
