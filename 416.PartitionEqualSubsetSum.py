class Solution:
    '''
    01背包问题
    比较难想到用dp 背包解决问题
    https://programmercarl.com/0416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.html#_416-%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86
    '''
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2 == 1:
            return False
        n = numSum // 2
        dp = [0]*(n+1)
        for i in range(len(nums)):
            currNum = nums[i]
            for j in range(n, currNum-1, -1):
                dp[j] = max(dp[j], dp[j-currNum]+currNum)
        return dp[n] == n