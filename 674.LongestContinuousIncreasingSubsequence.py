class Solution:
    '''
    Greedy
    Can use DP as well: if nums[i] > nums[i-1]: dp[i] = dp[i-1]+1
    '''
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLength = 1
        currLength = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                currLength = 1
        return maxLength