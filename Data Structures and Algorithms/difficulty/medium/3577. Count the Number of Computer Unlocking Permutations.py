from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        freq_count = {}

        for i in complexity:
            if i in freq_count:
                freq_count[i] += 1
            else:
                freq_count[i] = 1
        
        if 0 not in freq_count.keys():
            return 0
        

sol = Solution()
print(sol.countPermutations([3,3,3,4,4,4]))
