from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lst = list(zip(*strs))
        res = 0
        for i in lst:
            if sorted(i) != list(i):
                res += 1
        return res
