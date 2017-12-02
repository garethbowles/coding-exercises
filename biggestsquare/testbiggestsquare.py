#!/usr/bin/env python

import unittest
from biggestsquare import BiggestSquare

class TestBiggestSquare(unittest.TestCase):
    def test_rectangle(self):
        bs = BiggestSquare(7, 4)
        print 'Should get 1 for a 7x4 rectangle'
        self.assertEqual(bs.find_biggest_square(7, 4), 1)

    def test_rectangle2(self):
        bs = BiggestSquare(4, 6)
        print 'Should get 2 for a 4x6 rectangle'
        self.assertEqual(bs.find_biggest_square(4, 6), 2)

    def test_square(self):
        bs = BiggestSquare(3, 3)
        print 'Should get 3 for a 3x3 square'
        self.assertEqual(bs.find_biggest_square(3, 3), 3)

if __name__ == '__main__':
    unittest.main()
