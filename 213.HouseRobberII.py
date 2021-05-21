class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        maximum = max(self.rob1(nums[:(len(nums)-1)]), self.rob1(nums[1:]))
        return maximum


    def rob1(self, nums):
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], nums[i]+dp[i-1])
        return dp[len(nums)]