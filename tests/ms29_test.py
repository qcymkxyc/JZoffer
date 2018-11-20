import unittest
from main.question29 import my1
import numpy as np


class MSTestCase(unittest.TestCase):
    def setUp(self):
        self.matrix = np.arange(1, 17,dtype=np.float32).reshape(4, 4)
        self.r = [1.0, 2.0, 3.0, 4.0, 8.0, 12.0, 16.0, 15.0, 14.0, 13.0, 9.0, 5.0, 6.0, 7.0, 11.0, 10.0]

    def test_my1_clockwise_display(self):
        self.assertEqual(self.r, my1.clockwise_display(self.matrix))


if __name__ == '__main__':
    unittest.main()
