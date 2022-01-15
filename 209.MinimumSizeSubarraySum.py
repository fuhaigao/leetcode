class Solution:
    # Sliding Window
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        index, currSum, minLength = 0, 0, float('inf')
        for i in range(len(nums)):
            currSum += nums[i]
            while currSum >= target:
                minLength = min(minLength, i-index+1)
                currSum -= nums[index]
                index += 1
        return 0 if minLength == float('inf') else minLength