import unittest
from main.question58 import my1


class MSTestCase(unittest.TestCase):
    def test_my1_reverse_sentence(self):
        s = "I am a Student."
        r_s = "Student. a am I"
        self.assertEqual(r_s, my1.reverse_sentence(s))
        self.assertEqual("",my1.reverse_sentence(""))


if __name__ == '__main__':
    unittest.main()
