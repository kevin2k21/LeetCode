
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gen(op_brac,cl_brac,s):
            if op_brac == cl_brac and op_brac+cl_brac == n*2:
                res.append(s)
                return
            if op_brac < n:
                gen(op_brac+1,cl_brac,s+"(")
            if cl_brac < op_brac:
                gen(op_brac,cl_brac+1,s+")")
        gen(0,0,"")
        return res

sol = Solution()
print(sol.generateParenthesis(3))
