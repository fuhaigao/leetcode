class Solution:
    '''
    5 states:
    0. 没有买入
    1. 第一次买入
    2. 第一次卖出
    3. 第二次买入
    4. 第二次卖出
    dp[i][j]: ith day with state = j
    https://programmercarl.com/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.html#%E6%80%9D%E8%B7%AF
    '''
            
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*5 for i in range(n)]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, n):
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
        print(dp)
        return dp[-1][4]