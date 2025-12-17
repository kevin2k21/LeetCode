from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        j = 0
        res = []
        k = 0
        l = len(target)
        for i in range(1,n+1):
            if j >= l:
                break
            elif i < target[j]:
                res.append("Push")
            else:
                if j-1 == -1:
                    for k in range(1,target[j]):
                        res.append("Pop")
                    res.append("Push")
                    j += 1
                else:
                    for k in range(target[j-1],target[j]-1):
                        res.append("Pop")
                    res.append("Push")
                    j += 1

        return res
            
sol = Solution()
print(sol.buildArray([1,3],3))
