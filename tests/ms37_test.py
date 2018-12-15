import unittest
from main.question26 import my1 as q26
from main.question37 import my1, book1


class MSTestCase(unittest.TestCase):
    def setUp(self):
        self.pre_order = [1, 2, 4, 3, 5, 6]
        self.in_order = [4, 2, 1, 5, 3, 6]

        self.root = q26.create_binary_tree(self.pre_order, self.in_order)

    def test_my1_level_display(self):
        level_traverse = my1.level_display(self.root)
        for node in level_traverse:
            if not node:
                print(None)
            else:
                print(node)

    def test_my1_serialize_binary_tree(self):
        my1.serialize_binary_tree(self.root)

        my1.serialize_binary_tree(None)

    def test_my1_deserizlize_binary_tree(self):
        # 功能测试
        serialization_tree = my1.serialize_binary_tree(self.root)
        root = my1.deserialize_binary_tree(serialization_tree)
        self.assertEqual(my1.level_display(self.root), my1.level_display(root))

        # 边界测试
        serialization_tree = my1.serialize_binary_tree(None)
        root = my1.deserialize_binary_tree(serialization_tree)
        self.assertEqual(my1.level_display(None),my1.level_display(root))

    def test_book1_serialize(self):
        import os
        print(os.getcwd())
        # book1.serialize()


if __name__ == '__main__':
    unittest.main()
