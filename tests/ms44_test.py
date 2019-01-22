import unittest
from main.question44 import my1


class MSTestCase(unittest.TestCase):
    def test_my1_find_num(self):
        self.assertEqual(5, my1.find_num(5))
        self.assertEqual(1, my1.find_num(13))
        self.assertEqual(4, my1.find_num(19))

    def test_book1_find_num(self):
        self.assertEqual(5, my1.find_num(5))
        self.assertEqual(1, my1.find_num(13))
        self.assertEqual(4, my1.find_num(19))


if __name__ == '__main__':
    unittest.main()
