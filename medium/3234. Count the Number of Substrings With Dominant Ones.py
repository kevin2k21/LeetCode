class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            for j in range(i,n):
                zero = s[i:j+1].count('0')**2
                one = s[i:j+1].count('1')
                if zero <= one:
                    cnt += 1
        return cnt
