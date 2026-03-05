
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hash_table = {0:1}
        cur_sum = 0
        for i in nums:
            cur_sum += i
            if cur_sum-k in hash_table:
                count += hash_table[cur_sum - k]
            hash_table[cur_sum] = hash_table.get(cur_sum,0)+1
        
        return count

            
        
sol = Solution()
print(sol.subarraySum([1,1,1],2))
        