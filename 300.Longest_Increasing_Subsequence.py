class Solution:
    '''
    dp[i] longest inceasing subsequence till i
    transform function if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j]+1)
    traversal: two-loop: i for nums, j for 0-i-1
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)