class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        res = float('inf')
        for i in range(4):
            res = min(res, nums[len(nums)-4+i]-nums[i])
        return res
