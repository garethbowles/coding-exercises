#!/usr/bin/env python

import unittest
from binarytree import BTree
from node import Node

class TestBinaryTree(unittest.TestCase):
    def test_sum(self):
        tree = BTree()
        tree.root = Node(26)
        tree.root.left = Node(14)
        self.assertEqual(40, tree.sum(tree.root))

    def test_is_sumtree(self):
        tree = BTree()
        tree.root = Node(26)
        tree.root.left = Node(9)
        tree.root.left.left = Node(6)
        tree.root.left.right = Node(3)
        tree.root.right = Node(1)
        tree.root.right.right = Node(7)
        self.assertTrue(tree.isSumTree(tree.root))

    def test_is_not_sumtree(self):
        tree = BTree()
        tree.root = Node(26)
        tree.root.left = Node(14)
        tree.root.right = Node(22)
        self.assertFalse(tree.isSumTree(tree.root))

    def test_empty_tree_is_sumtree(self):
        tree = BTree()
        self.assertTrue(tree.isSumTree(tree.root))

    def test_leaf_node_is_sumtree(self):
        tree = BTree()
        tree.root = Node(12)
        self.assertTrue(tree.isSumTree(tree.root))

if __name__ == '__main__':
    unittest.main()
