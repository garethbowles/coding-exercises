#!/usr/bin/env python

import logging
import sys

__version__ = "0.0.1"

logging.basicConfig(level=logging.INFO)

class BiggestSquare(object):
    """
    Given a rectangular plot of land, find the biggest square plot such that
    the rectangle can be divided into squares with nothing left over.
    """

    def __init__(self, x, y):
        # Save the original dimensions
            self.x = x
            self.y = y

    def find_biggest_square(self, x, y):
        logging.debug("%d %d" % (x, y))
        # Find the longest side
        if x >= y:
            long_side = x
            short_side = y
        else:
            long_side = y
            short_side = x

        # Base case
        if long_side % short_side == 0:
            # We have a square, or row of squares
            logging.debug(short_side)
            return short_side

        # Recursive case - find biggest square in remaining area
        return self.find_biggest_square(long_side - short_side, short_side)

if __name__ == "__main__":
    length = 7
    width = 4
    obj = BiggestSquare(length, width)
    print "Biggest square that fits a %d by %d field is %s" % (obj.x, obj.y,
        obj.find_biggest_square(length, width))
