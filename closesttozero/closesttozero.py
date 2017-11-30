#!/usr/bin/env python

import logging
import sys

__version__ = "0.0.1"

logging.basicConfig(level=logging.DEBUG)

class ClosestPairToZero(object):
    """
    Given a 1-dimensional array that may contain both +ve and -ive integers,
    find the two numbers whose sum is closest to zero.
    """

    def __init__(self, numbers):
        self.numbers = numbers
        logging.debug(numbers)

    def find_smallest_pair_sum(self):
        # Starting with each number in turn, add it to each of the other numbers
        # in turn and keep track of the smallest value
        num_count = len(self.numbers)
        if num_count < 2:
            print "We need at least 2 numbers!"
            return

        smallest_sum = sys.maxint
        first_pos = 0
        second_pos = 0
        for start_pos in range(0, num_count - 1):
            for next_pos in range(start_pos + 1, num_count):
                current_sum = abs(self.numbers[start_pos] + self.numbers[next_pos])
                logging.debug("first %d, second %d, sum %d" %
                    (self.numbers[start_pos], self.numbers[next_pos],
                     current_sum))
                if current_sum < smallest_sum:
                    logging.debug("Changing smallest_sum to %d" % current_sum)
                    smallest_sum = current_sum
                    first_pos = start_pos
                    second_pos = next_pos

        return (smallest_sum, first_pos, second_pos)

if __name__ == "__main__":
    nums = [45, -43, 2, 6, -10]
    smallsum = ClosestPairToZero(nums)
    (smallest_sum, first_pos, second_pos) = smallsum.find_smallest_pair_sum()
    print "Smallest sum is %d, from elements %d and %d" % (smallest_sum,
        first_pos, second_pos)
