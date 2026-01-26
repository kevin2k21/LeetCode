from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = float('inf')
        for i in range(len(arr)-1):
            cur = arr[i+1]-arr[i]
            if cur < m:
                m = cur
        res = []

        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff <= m:
                res.append([arr[i],arr[i+1]])
        return res
    
sol = Solution()
print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
