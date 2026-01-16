from itertools import pairwise
from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hs = sorted([1] + hFences + [m])
        vs = sorted([1] + vFences + [n])

        h_dist = set()
        v_dist = set()

        for i in range(len(hs)):
            for j in range(i+1,len(hs)):
                h_dist.add(hs[j]-hs[i])

        for i in range(len(vs)):
            for j in range(i+1,len(vs)):
                v_dist.add(vs[j]-vs[i])

        common = v_dist&h_dist
        if not common:
            return -1
        else:
            return (max(common)**2)% (10**9 + 7)
        
sol = Solution()
print(sol.maximizeSquareArea(4,3,[2,3],[2]))
