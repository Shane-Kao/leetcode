# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'


class Solution:
    def maxArea(self, height) -> int:
        pass

    @staticmethod
    def _get_area(list_, start_idx, end_idx):
        val_ = list_[start_idx] if list_[start_idx] < list_[end_idx] else list_[end_idx]
        return val_ * (end_idx - start_idx)


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxArea(height=[1,1]) == 1
    assert solution.maxArea(height=[1,8,6,2,5,4,8,3,7]) == 49
    assert solution.maxArea(height=[4,3,2,1,4]) == 16
    assert solution.maxArea(height=[1,2,1]) == 2
