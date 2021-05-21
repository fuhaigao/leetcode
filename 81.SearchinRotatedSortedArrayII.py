class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[start] < nums[mid]:
                if target < nums[mid] and target >= nums[start] :
                    end = mid
                else:
                    start = mid+1
            elif nums[start] > nums[mid]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid+1
                else:
                    end = mid
            else:
                start += 1
        return True if nums[start] == target else False