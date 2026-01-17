from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        comb = list(zip(bottomLeft,topRight))
        flat = [tuple(a + b) for a, b in comb]

        l = len(comb)
        max_area = 0
        for i in range(l):
            for j in range(i+1,l):

                i_x_cords = (flat[i][0],flat[i][2])
                i_y_cords = (flat[i][1],flat[i][3])
                j_x_cords = (flat[j][0],flat[j][2])
                j_y_cords = (flat[j][1],flat[j][3])

                inter_x = min(i_x_cords[1],j_x_cords[1]) - max(i_x_cords[0],j_x_cords[0]) 
                inter_y = min(i_y_cords[1],j_y_cords[1]) - max(i_y_cords[0],j_y_cords[0]) 

                if inter_x <= 0 or inter_y <= 0:
                    continue

                max_area = max(max_area,min(inter_x,inter_y)**2)
                    
        return max_area
sol = Solution()
print(sol.largestSquareArea([[1,1],[2,2],[3,1]],[[3,3],[4,4],[6,6]]))
