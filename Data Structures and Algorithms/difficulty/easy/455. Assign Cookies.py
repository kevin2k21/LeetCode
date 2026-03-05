from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        l =  len(g)
        for i in s:
            if res <  l and i >= g[res]:
                res += 1
        return res
