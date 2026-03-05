from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l = len(nums)
        n = l//2
        num = {}
        for i in nums:
            num[i] = num.get(i,0)+1
            if num[i] == n:
                return i
