# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'


class Solution:
    def convert(self, input_string, numRows):
        if numRows == 1:
            return input_string
        output_string = ''
        length_ = len(input_string)
        for row_idx in range(numRows):
            col_idx = 1
            ele = row_idx
            while True:
                if ele > length_ - 1:
                    break
                output_string += input_string[ele]
                if row_idx == 0 or row_idx == numRows - 1:
                    ele += 2 * numRows - 2
                else:
                    ele += (2 * numRows - 2 - 2 * row_idx) if col_idx % 2 == 1 else 2 * row_idx
                col_idx += 1
        return output_string


if __name__ == '__main__':
    f = Solution().convert
    assert (f('A', 1) == 'A')
    assert (f("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    assert (f("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")


