from itertools import pairwise
from typing import List
from collections import defaultdict

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        diff = defaultdict(int)
        total = 0
        for x,y,l in squares:
            diff[y] += l
            diff[y+l] -= l
            total += l*l

        s = 0
        area = 0
        
        for y1,y2 in pairwise(sorted(diff)):
            s += diff[y1]
            area += s*(y2-y1)

            if area*2 >= total:
                return y2-(area*2 - total)/(2*s)
    
sol = Solution()
print(sol.separateSquares([[0,0,2],[1,1,1]]))
