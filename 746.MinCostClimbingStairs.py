class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*n
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n):
            oneStep = dp[i-1]+cost[i-1]
            twoStep = dp[i-2]+cost[i-2]
            dp[i] = min(oneStep, twoStep)
        return min(dp[n-2]+cost[n-2], dp[n-1]+cost[n-1])