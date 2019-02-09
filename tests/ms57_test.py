import unittest
from main.question57 import book1, my2


class MSTestCase(unittest.TestCase):
    def test_book1_pair_nums(self):
        nums = [1,2,4,7,11,15]
        s = 15

        self.assertEqual((4,11), book1.pair_nums(nums,s))
        self.assertIsNone(book1.pair_nums(nums,20))
        self.assertIsNone(book1.pair_nums(None,s))

    def test_sum_seq(self):
        s = 15
        seqs = [
            [1, 2, 3, 4, 5],
            [4, 5, 6],
            [7, 8]
        ]
        self.assertEqual(seqs, my2.sum_seq(s))
        self.assertEqual([], my2.sum_seq(16))


if __name__ == '__main__':
    unittest.main()
