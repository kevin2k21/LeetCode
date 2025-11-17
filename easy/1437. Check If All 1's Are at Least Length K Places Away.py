from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        prev = None
        for i,num in enumerate(nums):
            if num == 1 :
                if prev != None and(i-prev-1) < k:
                    return False
                else:
                    prev = i
        return True
    
