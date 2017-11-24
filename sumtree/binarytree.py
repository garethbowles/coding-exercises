#!/usr/bin/env python

import logging
from node import Node

__version__ = "0.0.1"

logging.basicConfig(level=logging.INFO)

"""
Binary tree class with utility functions:
"""

class BTree:
    def __init__(self):
        root = None

    # Return sum of node plus its left and right nodes
    def sum(self, node):
        if node is None:
            return 0

        return self.sum(node.left) + node.value + self.sum(node.right)

    # Return True if tree is a SumTree
    def isSumTree(self, node):
        # Empty tree or leaf node is defined as a SumTree
        if node is None or node.left is None or node.right is None:
            return True

        ls = self.sum(node.left)
        rs = self.sum(node.right)

        if node.value == ls + rs and self.isSumTree(node.left) and self.isSumTree(node.right):
            return True
        else:
            return False

if __name__ == "__main__":
    tree = BTree()
    tree.root = Node(26)
    tree.root.left = Node(14)
    tree.root.right = Node(12)
    logging.debug(tree.root.value)
