class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_count = float('inf')
        count = 0
        if len(s) == 1:
            return 0
        start = s.find('b')
        end = s.rfind('b')
        if start == end:
            if start == -1:
                return 0
            else:
                return 1
        if start == 0:
            start += 1
        for i in range(start,end):
            if s[i-1] != s[i]:
                count += 1
                min_count = min(count,i)

            else:
                min_count = min(count,i)
        return min_count
                
                
sol = Solution()
print(sol.minimumDeletions("bbaaaaabb"))