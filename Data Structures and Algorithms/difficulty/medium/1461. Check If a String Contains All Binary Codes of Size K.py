class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        comb = set()
        win = []
        for i in range(len(s)-k+1):
            win = s[i:i+k]
            comb.add(win)
        if len(comb) == 2**k:
            return True
        else:
            return False            
            

sol = Solution()
print(sol.hasAllCodes("01100110110",2))