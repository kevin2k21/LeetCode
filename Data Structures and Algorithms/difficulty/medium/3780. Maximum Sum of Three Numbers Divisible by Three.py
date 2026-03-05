from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        group = {0 : [], 1 : [], 2 : []}
        for i in nums:
            group[i%3].append(i)
        for i in group:
            group[i].sort(reverse = True)

        res = 0

        if len(group[0]) >= 3:
            res = max(res,sum(group[0][:3]))
        if len(group[1]) >= 3:
            res = max(res,sum(group[1][:3]))
        if len(group[2]) >= 3:
            res = max(res,sum(group[2][:3]))
        if len(group[0]) >= 1 and len(group[1]) >= 1 and len(group[2]) >= 1:
            res = max(res,(group[0][0]+group[1][0]+group[2][0]))


        return res
