def sortIntegers(nums):
    mergesort(nums)

def mergesort(nums):
    if len(nums) == 1:
        return
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    mergesort(left)
    mergesort(right)
    merge(nums, left, right)

def merge(nums, left, right):
    i, j, idx = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[idx] = left[i]
            i += 1
        else:
            nums[idx] = right[j]
            j += 1
        idx += 1
    while i < len(left):
        nums[idx] = left[i]
        i += 1
        idx += 1
    while j < len(right):
        nums[idx] = right[j]
        j += 1
        idx += 1
    return