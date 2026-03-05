from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(cost)):
            if tank < 0:
                start = i
                tank = 0
            tank = tank  + gas[i] - cost[i]
        return start
