import unittest

from main.面试题10 import my1
from main.面试题10 import book1
from main.面试题10 import book2

class MSTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_my1_fibonacci(self):
        """"""
        fibonacci_num = my1.fibonacci(9)
        self.assertEqual(34,fibonacci_num)

    def test_book1_fibonacci(self):
        fibonacci_num = book1.fibonacci(9)
        self.assertEqual(34,fibonacci_num)

    def test_book2_jump(self):
        n = 3
        self.assertEqual(3,book2.jump(n))


if __name__ == '__main__':
    unittest.main()
