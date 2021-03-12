# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'


class Solution:
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1
        while i != j and i < len(height):
            min_ = min(height[i], height[j])
            curr_area = (j - i) * min_
            if curr_area > max_area:
                max_area = curr_area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxArea(height=[1,1]) == 1
    assert solution.maxArea(height=[1,8,6,2,5,4,8,3,7]) == 49
    assert solution.maxArea(height=[4,3,2,1,4]) == 16
    assert solution.maxArea(height=[1,2,1]) == 2
    print(solution.maxArea(height=[2,3,4,5,18,17,6]))
    # assert solution.maxArea(height=[2,3,4,5,18,17,6]) == 17
