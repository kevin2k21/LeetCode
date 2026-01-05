from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        no_neg = 0
        smol = float('inf')
        for i in matrix:
            for j in i:
                num = abs(j)
                smol = min(smol,num)
                if j < 0:
                    res += num
                    no_neg += 1
                else:
                    res += j
        if no_neg % 2 == 0:
            return res
        else:
            return res-(smol*2)
        
sol = Solution()
print(sol.maxMatrixSum([[1,-1],[-1,1]]))
