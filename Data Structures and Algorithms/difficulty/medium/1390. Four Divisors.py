from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            temp = 0
            c = 0
            n = i//2 + 1
            for j in range(1,n):
                if i % j == 0:
                    temp += j
                    c += 1
                if c == 4:
                    break
            if c == 3:
                res += temp+i
        return res

sol = Solution()
print(sol.sumFourDivisors([1,2,3,4,5,6,7,8,9,10]))
