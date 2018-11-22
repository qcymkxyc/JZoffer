import unittest
from main.question31 import book1


class MSTestCase(unittest.TestCase):
    def test_book1_is_pop_seq(self):
        # 功能测试
        push_seq = [1, 2, 3, 4, 5]
        pop_seq = [4, 5, 3, 2, 1]
        self.assertTrue(book1.is_pop_seq(push_seq, pop_seq))

        push_seq = [1, 2, 3, 4, 5]
        pop_seq = [4, 3, 5, 1, 2]
        self.assertFalse(book1.is_pop_seq(push_seq, pop_seq))

        push_seq = [1, ]
        pop_seq = [1]
        self.assertTrue(book1.is_pop_seq(push_seq, pop_seq))

        # 边界测试
        with self.assertRaises(ValueError):
            push_seq = [1, 2, 3]
            pop_seq = [1, 2, 3, 5]
            book1.is_pop_seq(push_seq, pop_seq)

            push_seq = [1, 2, 3]
            pop_seq = [1, 2, 4]
            book1.is_pop_seq(push_seq, pop_seq)

            book1.is_pop_seq([1, 2, 3], None)
            book1.is_pop_seq(None, None)


if __name__ == '__main__':
    unittest.main()
