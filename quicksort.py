def quicksort(nums, low, high):
    if low < high:
        index = partition(nums, low, high)
        quicksort(nums, low, index-1)
        quicksort(nums, index+1, high)
    return nums
    

def partition(nums, low, high):
    index = low
    pivot = high
    for i in range(low, high):
        if nums[i] < nums[pivot]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
    nums[pivot], nums[index] = nums[index], nums[pivot]
    return index
    
nums = [5,6,8,3,4,9,2,1,7]
nums = quicksort(nums, 0, len(nums)-1)
print(nums)