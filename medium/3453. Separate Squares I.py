from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        min_y = float('inf')
        max_y = float('-inf')
        total = 0
        for x,y,a in squares:
            min_y = min(min_y,y)
            max_y = max(max_y,y+a)
            total += a * a
        
        half = total/2

        def low_area(line):
            area = 0
            for x,y,a in squares:
                if line <= y:
                    continue
                elif line >= y+a:
                    area += a*a
                else:
                    area += a*(line-y)
            return area
        
        while max_y - min_y > 1e-6:
            mid = (min_y+max_y)/2
            if low_area(mid) >= half:
                max_y = mid
            else:
                min_y = mid

        return min_y
    
sol = Solution()
print(sol.separateSquares([[0,0,2],[1,1,1]]))
