class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        s = s[::-1]
        s = int(s)
        return abs(s-n)
