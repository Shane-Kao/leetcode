# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import math
import bisect
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        g = (s[i: i + len_] for len_ in range(N, 0, -1) for i in range(N - len_ + 1))
        while True:
            curr_ = next(g)
            if curr_ == curr_[::-1]:
                return curr_




if __name__ == '__main__':
    f = Solution().longestPalindrome
    # print(f('babad'))
    assert (f('babad') == 'bab')
    assert (f('cbbd') == 'bb')
    assert (f('a') == 'a')
    assert (f('ac') == 'a')


