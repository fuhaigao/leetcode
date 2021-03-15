class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        first = self.findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = self.findLast(nums, target)
        return [first, last]
        
    def findFirst(self, nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return -1
        else:
            return left

    def findLast(self, nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[right] != target:
            return -1
        else:
            return right