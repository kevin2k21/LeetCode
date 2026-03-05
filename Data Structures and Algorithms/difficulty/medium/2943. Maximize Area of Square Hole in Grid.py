from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        length = 0
        max_len_hor = 0
        prev = 0
        for i in hBars:
            if prev == 0:
                length = 1

            elif i-1 == prev:
                length += 1
                
            else:
                max_len_hor = max(max_len_hor,length)
                length = 1

            prev = i

        max_len_hor = max(max_len_hor,length)

        prev = 0
        length = 0
        max_len_ver = 0
        for i in vBars:
            if prev == 0:
                length = 1

            elif i-1 == prev:
                length += 1

            else:
                max_len_ver = max(max_len_ver,length)
                length = 1

            prev = i
        
        max_len_ver = max(max_len_ver,length)
        
        return (min(max_len_hor,max_len_ver)+1)**2
    

sol = Solution()
print(sol.maximizeSquareHoleArea(3,13,[2,4,3],[4,6,7,12,10,13,2]))
