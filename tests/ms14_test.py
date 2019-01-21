import unittest

from main.question14 import my1


class MyTestCase(unittest.TestCase):

    def test_compute_max_mul(self):
        """测试最大绳子乘积"""
        # 正常情况
        self.assertEqual(my1.compute_max_mul(8), 18)
        # 绳子长度错误
        with self.assertRaises(ValueError):
            my1.compute_max_mul(-1)



if __name__ == '__main__':
    unittest.main()
