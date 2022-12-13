def quicksort(nums, start, end):
    if start >= end:
        return
    index, pivot = start, end
    for i in range(start, end):
        if nums[i] < nums[pivot]:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    nums[index], nums[pivot] = nums[pivot], nums[index]
    # print(nums, index)
    quicksort(nums, start, index-1)
    quicksort(nums, index+1, end)

def sortIntegers(nums):
    quicksort(nums, 0, len(nums)-1)

# arr = [5,3,4,2,6,1,9,8,7]
arr = [5,6,8,3,4,9,2,1,7]
sortIntegers(arr)
print(arr)