import unittest
from main.question49 import my1


class MSTestCase(unittest.TestCase):
    def test_my1_ugly_num(self):
        print(my1.ugly_num(1500))


if __name__ == '__main__':
    unittest.main()
