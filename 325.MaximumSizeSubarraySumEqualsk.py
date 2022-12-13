class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sumToIndex = collections.defaultdict(int)
        currSum = maxLength = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum == k:
                maxLength = max(maxLength, i+1)
            elif currSum-k in sumToIndex:
                startIndex = sumToIndex[currSum-k]
                maxLength = max(maxLength, i-startIndex)
            if currSum not in sumToIndex:
                sumToIndex[currSum] = i
        return maxLength