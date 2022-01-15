class Solution:
    '''
    greedy
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            result = max(result, currSum)
            if currSum <= 0:
                currSum = 0
        return result