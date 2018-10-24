import unittest

from main.question21 import my1, book1


class MSTestCase(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(10))

    @staticmethod
    def is_adjust(nums):
        """判断是否符合调整标准

        :param nums: list
            调整后的数组
        :return: bool
            是否符合
        """
        is_even = False     # 是否为偶数的标志
        for num in nums:
            if num % 2 == 0:
                is_even = True
            if is_even and num % 2 == 1:
                return False

        return True

    def test_my1_adjust_list(self):
        adjust_nums = my1.adjust_list(self.nums)
        self.assertTrue(MSTestCase.is_adjust(adjust_nums))

    def test_book1_adjust_list(self):
        book1.adjust_list(self.nums)
        self.assertTrue(MSTestCase.is_adjust(self.nums))


if __name__ == '__main__':
    unittest.main()
