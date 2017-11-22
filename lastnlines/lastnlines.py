#!/usr/bin/env python

import logging

__version__ = "0.0.1"

logging.basicConfig(level=logging.INFO)

class LastNLines(object):
    """
    Print the last n lines of a file,
    passing in the file contents as a string.
    """

    def __init__(self, lines_string, n):
        self.lines_string = lines_string
        self.n = n

    def get_last_n_lines(self):
        lines = []
        split_lines = self.lines_string.split('\n')
        # Check for no newlines
        if split_lines != []:
            # Print last n lines, or all lines in file if total lines < n
            if len(split_lines) < self.n:
                count = len(split_lines)
            else:
                count = self.n
            logging.debug("count = %d" % count)

            for i in range(0, count):
                logging.debug("i = %d, line = %s" % (i, split_lines[-count + i]))
                lines.append(split_lines[-count + i])
        return lines

if __name__ == "__main__":
    filestring = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8"
    num_lines = 6
    lines = LastNLines(filestring, num_lines)
    last_n_lines = lines.get_last_n_lines()
    for i in range(0, num_lines):
        print last_n_lines[i]
