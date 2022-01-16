class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        dp 01背包问题
        要想最后结果最小，就需要尽量分成同重量的两部分。此时就可以用背包方法解决
        https://programmercarl.com/1049.%E6%9C%80%E5%90%8E%E4%B8%80%E5%9D%97%E7%9F%B3%E5%A4%B4%E7%9A%84%E9%87%8D%E9%87%8FII.html#%E6%80%BB%E7%BB%93
        '''
        totalWeight = sum(stones)
        n = totalWeight//2
        dp = [0]*(n+1)
        for i in range(len(stones)):
            weight = stones[i]
            for j in range(n, weight-1, -1):
                dp[j] = max(dp[j], dp[j-weight]+weight)
            print(dp)
        return totalWeight - 2*dp[n]