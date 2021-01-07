# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import math
import bisect
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            bisect.insort(nums1, i)
        idx1 = math.ceil(len(nums1) / 2 - 1)
        idx2 = math.floor(len(nums1) / 2)
        med_ = (nums1[idx1] + nums1[idx2])/2
        return med_


if __name__ == '__main__':
    f = Solution().findMedianSortedArrays

    assert (f([0, 0], [0, 0]) == 0.0)
    assert (f([1, 3], [2]) == 2.0)
    assert (f([1, 2], [3, 4]) == 2.5)
    assert (f([100], [2, 101]) == 100.0)
    assert (f([100], [2, 3]) == 3.0)
    assert(f([1], [2, 3]) == 2.0)
    assert(f([7], [2, 3]) == 3.0)
    assert(f([1, 3, 4], [3, 3]) == 3.0)
    assert(f([1, 2, 4, 78], [3]) == 3.0)
    assert(f([1, 3, 3, 78], [3]) == 3.0)
    assert(f([1, 3, 10], [9]) == 6.0)
    assert(f([1, 3, 10], [11]) == 6.5)
    assert (f([1, 3, 10], [11, 100]) == 10.0)
    assert(f([3, 10], [9]) == 9.0)
    assert (f([3, 10], [1]) == 3.0)
    assert (f([3, 10], [2, 11]) == 6.5)
    assert(f([3, 10], [11]) == 10.0)
    #
