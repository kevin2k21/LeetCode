from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        first = nums[0]
        s = sum(nums[1:])
        if ((s-first) % 2) == 0:
            return len(nums)-1
        return 0
