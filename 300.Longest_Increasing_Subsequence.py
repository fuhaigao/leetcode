class Solution:
    '''
    dp[i] longest inceasing subsequence till i
    transform function if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j]+1)
    traversal: two-loop: i for nums, j for 0-i-1
    '''
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1]*n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #     return max(dp)

    # 用binary search 优化, similar to 354
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0]*len(nums)
        size = 0
        res = 0
        for num in nums:
            l, r = 0, size
            while l < r:
                mid = (l+r) // 2
                if num > tails[mid]:
                    l += 1
                else:
                    r = mid
            tails[l] = num
            size = max(size, l+1)
        return size
