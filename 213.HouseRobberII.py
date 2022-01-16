class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        rob1 = self.robHelper(nums[:len(nums)-1])
        rob2 = self.robHelper(nums[1:len(nums)])
        return max(rob1, rob2)
    
    def robHelper(self, nums):
        n = len(nums)
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[n]