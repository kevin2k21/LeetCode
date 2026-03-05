from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_len = 0
        max_area = 0
        for i in range(len(bottomLeft)):
            xi1 , yi1 = bottomLeft[i]
            xi2 , yi2 = topRight[i]
            if xi2 - xi1 < max_len or yi2 - yi1 < max_len:
                continue
            for j in range(i+1,len(bottomLeft)):
                xj1 , yj1 = bottomLeft[j]
                xj2 , yj2= topRight[j]
                if xj2 - xj1 < max_len or yj2 - yj1 < max_len:
                    continue
                
                inter_x = min(xj2,xi2) - max(xj1,xi1)
                inter_y = min(yj2,yi2) - max(yj1,yi1)

                if inter_x <= 0 or inter_y <= 0:
                    continue

                max_len = max(max_len,min(inter_x,inter_y))

            max_area = max_len**2
            
        return max_area
    
sol = Solution()
print(sol.largestSquareArea([[1,1],[2,2],[3,1]],[[3,3],[4,4],[6,6]]))
