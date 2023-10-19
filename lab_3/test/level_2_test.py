import unittest
from lab_3.src.level_2 import inverting_tree,BinaryTree


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(1)
        self.root.left = BinaryTree(2)
        self.root.right = BinaryTree(3)
        self.root.left.left = BinaryTree(4)
        self.root.left.right = BinaryTree(5)
        self.root.right.left = BinaryTree(6)
        self.root.right.right = BinaryTree(7)

    def test_inverting_tree(self):
        inverted_root = inverting_tree(self.root)
        self.assertEqual(inverted_root.data, 1)
        self.assertEqual(inverted_root.left.data, 3)
        self.assertEqual(inverted_root.right.data, 2)
        self.assertEqual(inverted_root.left.left.data, 7)
        self.assertEqual(inverted_root.left.right.data, 6)
        self.assertEqual(inverted_root.right.left.data, 5)
        self.assertEqual(inverted_root.right.right.data, 4)


if __name__ == '__main__':
    unittest.main()
