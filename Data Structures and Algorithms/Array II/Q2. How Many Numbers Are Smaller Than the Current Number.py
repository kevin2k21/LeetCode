from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0]*101
        size = len(nums)
        for i in nums:
            freq[i]+=1

        for i in range(1,101):
            freq[i] += freq[i-1]
        
        res = [0] * size
        for i in range(size):
            t = nums[i]
            if t == 0:
                res[i] = 0
            else:
                res[i] = freq[t-1]
        return res
