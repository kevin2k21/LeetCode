class Solution:
    def countCollisions(self, directions: str) -> int:
        i = 0
        coli = 0
        stk = []
        s = list(directions.lstrip('L'))
        while i < len(s):
            cur = s[i]
            i += 1
            if cur == 'S':
                coli += len(stk)
                stk = []
                continue
            elif cur == 'L':
                coli += len(stk)
                coli += 1
                stk = []
                continue
            stk.append(cur)
        return coli

sol = Solution()
print(sol.countCollisions("RLRSLL"))
