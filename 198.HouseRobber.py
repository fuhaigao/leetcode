class Solution:
    '''
    dp[i]: maximum robbed money at ith house
    transform function: dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[n]