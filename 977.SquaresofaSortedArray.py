class Solution:
    # Two pointers
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, index = 0, len(nums)-1, len(nums)-1
        result = [-1]*len(nums)
        while left <= right:
            ls = nums[left]*nums[left]
            rs = nums[right]*nums[right]
            if ls >= rs:
                result[index] = ls
                left += 1
            else:
                result[index]= rs
                right -= 1
            index -= 1
        return result