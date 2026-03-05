from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        win = set()
        t = len(nums)
        for i in range(t-1,-1,-1):
            if nums[i] not in win:
                win.add(nums[i])
            else:
                break
            t = i
        return (t+2)//3

        