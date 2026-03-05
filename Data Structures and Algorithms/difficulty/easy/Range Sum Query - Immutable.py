from typing import List

class NumArray:
    prefix = []
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for i in nums:
            self.prefix.append(self.prefix[-1]+i)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]