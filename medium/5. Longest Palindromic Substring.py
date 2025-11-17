class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        m = 0
        start = 0
        for i in range(n):
            for j in range(i,n):
                s1 = s[i:j+1]
                if s1 == s1[::-1]:
                    if len(s1) > m:
                        m = len(s1)
                        start = i
        return s[start:start+m]

