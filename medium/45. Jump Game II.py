from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        cur_end = nums[0]
        max_jump = 0
        jump = 1
        if l <= 1:
            return 0
        for i in range(l-1):
            if max_jump < i+nums[i]:
                max_jump = i + nums[i]
            if i == cur_end:
                cur_end = max_jump
                jump += 1
        return jump
