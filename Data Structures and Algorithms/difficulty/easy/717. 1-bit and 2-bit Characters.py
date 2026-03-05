from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        flag = 0
        while i < n:
            if bits[i] == 0:
                i += 1
                flag = 0
            else:
                i += 2
                flag = 1
        if flag == 0:
            if bits[-1] == 0:
                return True
            else:
                return False
        else:
            return False
