class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        for i in s.split('0'):
            n = len(i)
            count += n*(n+1)
        return (count//2) % (10**9 + 7)
