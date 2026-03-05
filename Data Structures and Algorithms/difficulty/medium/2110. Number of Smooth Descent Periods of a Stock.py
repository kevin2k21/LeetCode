from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        j = 0
        res = 0
        l = len(prices)
        for i in range(l-1):
            if prices[i] - prices[i+1] == 1:
                j += 1
                res += j
            else:
                j = 0
        return res+l

