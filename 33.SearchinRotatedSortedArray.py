# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         # Binary Search find the rotate point (Smallest value)
#         low, high = 0, len(nums)-1
#         while low < high:
#             mid = (low+high)//2
#             if nums[mid] > nums[high]:
#                 low = mid+1
#             else:
#                 high = mid

#         # check which half is the target in
#         start = low
#         low, high = 0, len(nums)-1
#         if target >= nums[start] and target <= nums[high]:
#             low = start
#         else:
#             high = start
        
#         # Normal Binary search to find the target
#         while low < high:
#             mid = (low + high) // 2
#             if target > nums[mid]:
#                 low = mid+1
#             else:
#                 high = mid
#         return low if nums[low] == target else -1
    
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
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
        return start if nums[start] == target else -1
    