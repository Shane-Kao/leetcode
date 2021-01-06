# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sub_nums1 = nums1[round(len(nums1)/4): round(len(nums1)/4) + 2]
        nums1_len = len(nums1)
        while True:
            med_ = 2 * sub_nums1[0]/2 if nums1_len % 2 == 1 else (sub_nums1[0] + sub_nums1[1])/2
            try:
                n = nums2.pop()
                nums1_len += 1
                if len(sub_nums1) == 1:
                    if n <= sub_nums1[0]:
                        sub_nums1 = [n, sub_nums1[0]]
                    else:
                        sub_nums1 = [sub_nums1[0], n]
                else:
                    if n >= sub_nums1[1]:
                        pass
                    elif n <= sub_nums1[0]:
                        pass
                    else:
                        sub_nums1 = [n, sub_nums1[1]] if nums1_len%2 == 1 else [sub_nums1[0], n]
            except IndexError:
                return med_


if __name__ == '__main__':
    f = Solution().findMedianSortedArrays
    assert (f([100], [2, 101]) == 100.0)
    assert (f([100], [2, 3]) == 3.0)
    assert(f([1], [2, 3]) == 2.0)
    assert(f([7], [2, 3]) == 3.0)
    assert(f([1, 3, 4], [3, 3]) == 3.0)
    assert(f([1, 2, 4, 78], [3]) == 3.0)
    assert(f([1, 3, 3, 78], [3]) == 3.0)
    assert(f([1, 3, 10], [9]) == 6.0)
    assert(f([1, 3, 10], [11]) == 6.5)
    print(f([1, 3, 10], [11, 100]))
    assert (f([1, 3, 10], [11, 100]) == 10.0)
    assert(f([3, 10], [9]) == 9.0)
    assert (f([3, 10], [1]) == 3.0)
    assert (f([3, 10], [2, 11]) == 6.5)
    print(f([3, 10], [11]))
    assert(f([3, 10], [11]) == 10.0)

