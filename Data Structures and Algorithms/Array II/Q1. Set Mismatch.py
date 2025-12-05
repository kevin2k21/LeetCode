from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = max(nums)
        length = len(nums)
        d = {i: 0 for i in range(1,length+1)}
        rep = -1
        for i in nums:
            d[i] += 1
            if d[i] == 2:
                rep = i
        mis = -1
        for i in d:
            if d[i] == 0:
                mis = i
        return [rep,mis]

