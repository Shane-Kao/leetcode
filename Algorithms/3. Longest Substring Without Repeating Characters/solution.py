# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        g = (i for i in s)
        sub_string = ""
        while True:
            try:
                current_ = next(g)
                if current_ not in sub_string:
                    if output <= len(sub_string):
                        output += 1
                    sub_string += current_
                else:
                    sub_string = sub_string[sub_string.index(current_) + 1:] + current_
            except StopIteration:
                return output


if __name__ == '__main__':
    f = Solution().lengthOfLongestSubstring
    print(f("abcabcbb")) #3 abc
    print(f("bbbbb")) #1
    print(f("pwwkew")) #3 wke
    print(f("")) #0
    print(f("aab")) #2
    print(f("dvdf")) #3
    print(f("tmmzuxt")) #5
    print(f("ohvhjdml")) #6
    print(f("wobgrovw")) #6