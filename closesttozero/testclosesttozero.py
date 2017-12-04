#!/usr/bin/env python

import unittest
from closesttozero import ClosestPairToZero

class TestClosestPairToZero(unittest.TestCase):
    def test_all_different(self):
        numbers = [43, -45, 6, 2, 10]
        result = ClosestPairToZero(numbers).find_smallest_pair_sum()
        print 'Should get 2, for 1st and 2nd elements'
        self.assertEqual(result, (2, 0, 1))

    def test_all_same(self):
        numbers = [43, 43, 43, 43, 43]
        result = ClosestPairToZero(numbers).find_smallest_pair_sum()
        print 'Should get 86, for 1st and 2nd elements'
        self.assertEqual(result, (86, 0, 1))

    def test_only_one_number(self):
        numbers = [10]
        with self.assertRaises(Exception) as context:
            result = ClosestPairToZero(numbers).find_smallest_pair_sum()
        self.assertTrue('We need at least 2 numbers!' in context.exception)

if __name__ == '__main__':
    unittest.main()
