from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        s = sum(apple)
        res = 0
        while capacity:
            s -= capacity[0]
            res += 1
            capacity.pop(0)
            if s <= 0:
                break
        return res


sol = Solution()
print(sol.minimumBoxes([9,8,8,2,3,1,6],[10,1,4,10,8,5]))
