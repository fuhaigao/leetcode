class Solution:
    '''
    DP 完全背包
    dp[i]: the minimum number of coins to make up amount i
    transform function: dp[j] = min(dp[j], dp[j-coins[i]]+1)
    init: dp[0] = 0, other = max_int
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[amount] if dp[amount] != float('inf') else -1