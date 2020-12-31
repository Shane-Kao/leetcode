# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        start_idx_ = 0
        for i, j in enumerate(s):
            if j not in s[start_idx_: i]:
                if output <= i - start_idx_:
                    output += 1
            else:
                start_idx_ += s[start_idx_: i].index(j) + 1
        return output


if __name__ == '__main__':
    import time
    f = Solution().lengthOfLongestSubstring
    start_ = time.time()
    for _ in range(1000):
        assert f("abcabcbb") == 3 #3 abc
        assert f("bbbbb") == 1 #1
        assert f("pwwkew") == 3 #3 wke
        assert f("") == 0 #0
        assert f("aab") == 2 #2
        assert f("dvdf") == 3 #3
        assert f("tmmzuxt") == 5 #5
        assert f("ohvhjdml") == 6 #6
        assert f("wobgrovw") == 6 #6
        assert f("ggububgvfk") == 6  # 6
    print(time.time() - start_)