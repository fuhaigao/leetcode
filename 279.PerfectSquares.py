class Solution:
    '''
    dp[i]: minimum number of squres that sum to i
    transform function: dp[j] = min(dp[j], dp[j-i*i]+1)
    init: dp[0] = 0, other = max_int
    iteration: two-loop - one for perfect sqr numbers, one for n
    '''
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for i in range(1, n): # 遍历物品
            if i * i > n:
                break
            num = i * i
            for j in range(num, n + 1): # 遍历背包
                dp[j] = min(dp[j], dp[j - num] + 1)

        return dp[n]