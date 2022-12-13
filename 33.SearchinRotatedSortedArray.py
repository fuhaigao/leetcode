'''
先判断哪半边是sorted order
if target 在sorted 半边，更新 left/right
else 在另外半边
'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] < nums[mid]:
                if target < nums[mid] and target >= nums[start]:
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
