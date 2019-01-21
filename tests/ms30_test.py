import unittest
from main.question30 import my1, book1


class MSTestCase(unittest.TestCase):
    def test_my1_stack(self):
        stack = my1.Stack()
        stack.push(0)
        stack.push(1)
        self.assertEqual(0, stack.min())

        with self.assertRaises(ValueError):
            s = my1.Stack()
            s.min()

        stack = my1.Stack()
        stack.push(5)
        stack.push(4)
        stack.push(3)
        stack.push(2)
        stack.push(1)
        self.assertEqual(1, stack.pop())
        # 出栈无法实现O（1）的寻找最小值的指针
        self.assertEqual(2, stack.min())

    def test_book1_stack(self):
        stack = book1.Stack()
        with self.assertRaises(IndexError):
            stack.min()
            stack.pop()

        stack.push(3)
        self.assertEqual(3, stack.min())
        stack.push(4)
        self.assertEqual(3, stack.min())
        stack.push(2)
        stack.push(1)
        self.assertEqual(1, stack.min())
        self.assertEqual(1, stack.pop())
        self.assertEqual(2, stack.min())
        self.assertEqual(2, stack.pop())
        stack.push(0)
        self.assertEqual(0, stack.min())


if __name__ == '__main__':
    unittest.main()
