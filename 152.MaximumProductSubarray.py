class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                currMax, currMin = currMin, currMax
            nextMax = currMax*nums[i]
            nextMin = currMin*nums[i]
            currMax = max(nums[i], nextMax)
            currMin = min(nums[i], nextMin)
            res = max(currMax, res)
        return res
            
        