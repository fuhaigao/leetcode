class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: (x[0]-x[1]))
        minCost = 0
        for i, cost in enumerate(costs):
            if i < len(costs)/2:
                minCost += cost[0]
            else:
                minCost += cost[1]
        return minCost
        