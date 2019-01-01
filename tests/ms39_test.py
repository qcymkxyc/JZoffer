import unittest
from main.question39 import my1


class MSTestCase(unittest.TestCase):
    def test_my1_max_count_num(self):
        seq = [1, 2, 3, 2, 2, 2, 5, 4, 2]
        self.assertEqual(2, my1.max_count_num(seq))

        seq = [0]
        self.assertEqual(0, my1.max_count_num(seq))


if __name__ == '__main__':
    unittest.main()
