from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        stack = [0]               # sentinel 0
        for num in nums:
            # remove larger values that cannot contribute further
            while stack and stack[-1] > num:
                stack.pop()
            # if this number is a new positive layer, it costs 1 operation
            if not stack or stack[-1] < num:
                ans += 1
                stack.append(num)
        return ans
