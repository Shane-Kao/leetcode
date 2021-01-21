# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'


class Solution:
    def _get_index(self, input_string, row_idx, numRows):
        output_string = ''
        length_ = len(input_string)
        col_idx = 1
        ele = row_idx
        while True:
            if ele > length_ - 1:
                break
            output_string += input_string[ele]
            if row_idx == 0 or row_idx == numRows - 1:
                ele += (2 * numRows - 2)
            else:
                ele += (2 * numRows - 2 - 2 * row_idx) if col_idx % 2 == 1 else 2 * row_idx
            col_idx += 1
        return output_string

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            output_string = ''
            for row_idx in range(numRows):
                output_string += self._get_index(input_string=s, row_idx=row_idx, numRows=numRows)
            return output_string


if __name__ == '__main__':
    f = Solution().convert
    assert (f('A', 1) == 'A')
    assert (f("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    assert (f("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")


