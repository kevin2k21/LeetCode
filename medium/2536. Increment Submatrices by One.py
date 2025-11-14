from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        l = []
        for i in range(n):
            row = [0]*(n+1)
            l.append(row)
        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2+1):
                l[r][c1] += 1
                l[r][c2+1] -= 1
        ans = []
        for i in range(n):
            row = [0]*(n)
            ans.append(row)
        for r in range(n):
            run = 0
            for c in range(n):
                run += l[r][c]
                ans[r][c] = run
        return ans
            
