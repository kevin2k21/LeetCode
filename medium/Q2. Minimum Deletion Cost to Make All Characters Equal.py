from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c = {i : 0 for i in s}
        for i in range(len(s)):
            c[s[i]] += cost[i]
        l = []
        for i in c:
            l.append(c[i])
        l.sort()
        return sum(l[:-1])
        
