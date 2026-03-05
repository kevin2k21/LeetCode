from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5 : 0, 10 : 0, 20 : 0}
        for i in bills:
            if i == 5:
                cash[5] += 1
            elif i == 10:
                cash[10] += 1
                cash[5] -= 1
            else:
                cash[20] += 1
                if cash[10]>0:
                    cash[10] -= 1
                    cash[5] -= 1
                else:
                    cash[5] -= 3
            if cash[5] < 0:
                return False
        return True
