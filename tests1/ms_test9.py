import unittest
from main1.question9 import book1, book2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_book1_queue(self):
        queue = book1.Queue1()

        queue.append_tail(5)
        self.assertEqual(5, queue.delete_head())
        self.assertEqual(0, len(queue))

        nums = [1, 2, 3]
        for i, v in enumerate(nums):
            queue.append_tail(v)

        pop_list = list()
        while len(queue) > 0:
            pop_list.append(queue.delete_head())
        self.assertEqual(pop_list, nums)

    def test_book2_stack(self):
        nums = [1, 2, 3]
        pop_list = list()

        stack = book2.Stack()
        for i, v in enumerate(nums):
            stack.push(v)

        while len(stack) > 0:
            pop_list.append(stack.pop())
        nums.reverse()
        self.assertEqual(nums, pop_list)

        stack = book2.Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.pop())


if __name__ == '__main__':
    unittest.main()
