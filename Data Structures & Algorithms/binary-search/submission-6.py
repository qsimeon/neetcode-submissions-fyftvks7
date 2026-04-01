from typing import Optional
import numpy as np

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # NOTE: `nums` is already sorted in ascending order!
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        # Search only the left or right depending on whether the target is 
        # larger or smaller than the mid-point value in the list
        mid_idx = len(nums) // 2
        mid_val = nums[mid_idx]
        if target == mid_val:
            return mid_idx
        if target < mid_val:
            return self.search(nums[:mid_idx], target) # does not include mid_idx
        elif target >= mid_val:
            res = self.search(nums[mid_idx+1:], target)
            if res == -1:
                return -1
            else:
                return (mid_idx+1) + res
        return -1