from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        n = len(nums)
        if ones > 0:#if 1 exists then number of operations = n - no_of_ones_in_list
            return n - ones
        
        check = 0
        for i in nums:#check if gcd of list is 1 else return -1
            check = gcd(check,i)

        if check != 1:
            return -1
        
        mini = float("inf")
        #find min no of ops to create 1 using gcd = length of gcd 1 subarray - 1
        for i in range(n):#finds sub array staring from first till end
            cur = 0
            for j in range(i,n):#find subarray until cur = 1
                cur = gcd(cur,nums[j])
                if cur == 1:
                    length = j - i + 1#length of subarray formula
                    mini = min(mini,length)#finds length of least sub array if already found subarray
                    break
            if mini == 1:
                break
        return (mini-1)+(n-1)# no_of_ops = length of subarray - 1 + n - no_of_ones_in_list(ie 1)
