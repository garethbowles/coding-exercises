#!/usr/bin/env python

import unittest
from lastnlines import LastNLines

class TestLastNLines(unittest.TestCase):
    def test_multi_lines(self):
        file_string = (
            'str1\nstr2\nstr3\nstr4\nstr5\nstr6\nstr7\nstr8\nstr9\nstr10\nstr11'
            '\nstr12\nstr13\nstr14\nstr15\nstr16\nstr17\nstr18\nstr19\nstr20'
            '\nstr21\nstr22\nstr23\nstr24\nstr25')
        result = LastNLines(file_string, 6)
        print 'Last 6 lines of 25-line file'
        self.assertEqual(result.get_last_n_lines(), ['str20', 'str21',
            'str22', 'str23', 'str24', 'str25'])

    def test_not_enough_lines(self):
        file_string = 'str1\nstr2\nstr3\nstr4\nstr5'
        result = LastNLines(file_string, 6)
        print 'Print all 5 lines when asked for last 6 lines of 5-line file'
        self.assertEqual(result.get_last_n_lines(), ['str1', 'str2', 'str3',
            'str4', 'str5'])

    def test_newline_only(self):
        file_string = '\n'
        result = LastNLines(file_string, 6)
        print 'Print 2 null strings when file only contains a newline'
        self.assertEqual(result.get_last_n_lines(), ['', ''])

    def test_empty_file(self):
        file_string = ''
        result = LastNLines(file_string, 6)
        print 'Print null string when file is empty'
        self.assertEqual(result.get_last_n_lines(), [''])

if __name__ == '__main__':
    unittest.main()
