# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import numpy as np

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = np.array(["P", "A", "Y"])
        b = np.array((None, "P", None))
        np.column_stack((a, b))



if __name__ == '__main__':
    f = Solution().convert
    assert (f("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    assert (f("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
    assert (f('A', 1) == 'A')



