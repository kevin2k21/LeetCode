from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mon = [0] * n
        mon[0] = nums[0]
        mon[1] = nums[1]
        for i in range(2,n):
            mon[i] = max(mon[i-1],nums[i]+mon[i-2])
        return mon[-1]
