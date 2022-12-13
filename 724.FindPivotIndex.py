class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numSum = sum(nums)
        currSum = 0
        for i in range(len(nums)):
            if i > 0:
                currSum += nums[i-1]
            if (numSum-nums[i])/2 == currSum:
                return i
        return -1