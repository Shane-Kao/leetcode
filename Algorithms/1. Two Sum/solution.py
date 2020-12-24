# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = 0
        while True:
            try:
                ele = nums.pop(0)
                try:
                    return [idx, nums.index(target - ele) + idx + 1]
                except ValueError:
                    idx += 1
            except IndexError:
                break
