from typing import List

class Solution:
    def coinChange(self, coins, amount):
        memo = {}

        def dp(res):
            if res == 0:
                return 0
            if res < 0:
                return float('inf')
            if res in memo:
                return memo[res]
            
            ans = float('inf')
            
            for i in coins:
                ans = min(ans,dp(res-i)+1)
            
            memo[res] = ans
            return ans

        res = dp(amount)
        return res if res != float('inf') else -1



    
sol = Solution()
print(sol.coinChange([186,419,83,408],6249))
