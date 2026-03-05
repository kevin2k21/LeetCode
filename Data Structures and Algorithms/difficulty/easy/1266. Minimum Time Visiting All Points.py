from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)-1):
            a,b = points[i][0],points[i][1]
            c,d = points[i+1][0],points[i+1][1]
            dis_x = abs(c - a)
            dis_y = abs(d - b)
            if dis_x > dis_y:
                res += dis_y + (dis_x - dis_y)
            elif dis_y > dis_x:
                res += dis_x + (dis_y - dis_x)
            else:
                res += dis_x
        
        return res


sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))

