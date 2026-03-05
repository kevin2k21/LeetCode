from typing import List

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        l = float('inf')
        win = []
        s = 0
        left = 0
        for right in range(len(nums)):
            '''while nums[right] in win:
                win.remove(nums[left])
                s -= nums[left]
                left += 1'''
            if nums[right] in win:
                win.append(nums[right])
            else:
                win.append(nums[right])
                s += nums[right]

            while s >= k:
                l = min(l,right - left+1)
                win.remove(nums[left])
                s -= nums[left]
                left += 1
                if l == 1:
                    return l
        if l == float('inf'):
            return -1
        return l


sol = Solution()
print(sol.minLength([2,2,3,1],4))
