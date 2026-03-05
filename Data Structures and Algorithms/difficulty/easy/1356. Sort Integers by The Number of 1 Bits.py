from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num :(num.bit_count(),num))
        return arr




sol = Solution()
print(sol.sortByBits([10000,10000]))