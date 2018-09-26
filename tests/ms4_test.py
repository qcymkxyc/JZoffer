import unittest

from main.面试题4 import m1
from main.面试题4 import b1
from main.面试题4 import m2

class MSTest(unittest.TestCase):
    def setUp(self):
        self.n = [
            [1, 2, 8, 9],
            [2, 4, 9, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15]
        ]

    def test_run_m(self):
        num = 13
        self.assertTrue(m1.f(self.n, num))
        num = 7
        self.assertTrue(m1.f(self.n, num))
        num = 17
        self.assertFalse(m1.f(self.n, num))

    def test_run_b1(self):
        num = 7
        self.assertTrue(b1.f(self.n, num))

    def test_run_b2(self):
        num = 7
        self.assertTrue(m2.f(self.n,num))

        num = 13
        self.assertTrue(m2.f(self.n,num))

        num = 17
        self.assertFalse(m2.f(self.n,num))

    def tearDown(self):
        pass