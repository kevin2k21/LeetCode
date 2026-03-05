class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        prime = {2,3,5,7,11,13,17,19}# 10^6 can be represented 20bits so max number of count is 20 
        for i in range(left,right+1):
            num = bin(i)[2:]
            n = num.count('1')
            if n in prime:
                count += 1
        return count