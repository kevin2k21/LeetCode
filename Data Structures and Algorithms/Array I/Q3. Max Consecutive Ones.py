from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        prev = 0
        for i in nums:
            if i == 1:
                prev += 1
            else:
                m = max(m,prev)
                prev = 0
        
        return max(m,prev)
