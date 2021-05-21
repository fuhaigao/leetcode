class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum = 0
        for i in range(len(gas)):
            sum += gas[i]
            sum -= cost[i]
        if sum < 0:
            return -1
        
        tank, start = 0, 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                tank = 0
                start = i+1
        return start