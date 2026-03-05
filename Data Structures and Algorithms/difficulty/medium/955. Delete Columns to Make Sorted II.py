from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l = list(zip(*strs))
        res = 0
        for i in range(len(l)):
            val = 0
            for j in range(len(l[i])):
                temp = val
                val = ord(l[i][j])
                if temp > val:
                    res += 1
                    break
        return res


sol = Solution()
print(sol.minDeletionSize(["xc","yb","za"]))
