from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = []
        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(len1):
            dp.append([])
            for j in range(len2):
                dp[i].append(float('-inf'))
        for i in range(len1):
            for j in range(len2):
                prod = nums1[i]*nums2[j]
                dp[i][j] = prod
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j],prod+dp[i-1][j-1])
                if i > 0:
                    dp[i][j] = max(dp[i][j],dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j],dp[i][j-1])
        
        return dp[-1][-1]
        

