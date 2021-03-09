class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Binary Search find the rotate point (Smallest value)
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid

        # check which half is the target in
        start = low
        low, high = 0, len(nums)-1
        if target >= nums[start] and target <= nums[high]:
            low = start
        else:
            high = start
        
        # Normal Binary search to find the target
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid+1
            else:
                high = mid
        return low if nums[low] == target else -1