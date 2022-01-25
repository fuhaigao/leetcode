class Solution:
    # Basic approach, can be optimized using binary search
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        direction = nums[1] - nums[0]
        for i in range(1, len(nums)):
            currDirection = nums[i] - nums[i-1]
            if direction*currDirection<0 and direction > 0:
                return i-1
            direction = currDirection
        return len(nums)-1 if direction > 0 else 0