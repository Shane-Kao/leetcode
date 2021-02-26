# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        try:
            return re.match(p, s).group() == s
        except:
            return False


if __name__ == '__main__':
    solution = Solution()
    assert not solution.isMatch(s="aa", p="a")
    assert solution.isMatch(s="aa", p="a*")
    assert solution.isMatch(s="ab", p=".*")
    assert solution.isMatch(s="aab", p="c*a*b")
    assert not solution.isMatch(s="mississippi", p="mis*is*p*.")
