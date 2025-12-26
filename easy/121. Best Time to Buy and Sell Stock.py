from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = float('inf')
        res = 0
        for i in prices:
            if i < min_cost:
                min_cost = i
            res = max(res,i - min_cost)
        return res
