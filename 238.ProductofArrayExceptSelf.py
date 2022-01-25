class Solution:
    '''
    Divide into two parts: left and right
    e.g. 3 at index 2 = left[2] * right[2], where left[2] = nums[0]*nums[1], right[2] = nums[3]
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        result = [0]*len(nums)
        for i in range(len(nums)):
            result[i] = left[i]*right[i]
        return result
        