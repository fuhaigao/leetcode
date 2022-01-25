class Solution:
    # double Q 496, 2遍单调栈
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0]
        result = [-1]*len(nums)
        for i in range(1, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                result[index] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                result[index] = nums[i]
        return result
    
# Cleaner Code
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         dp = [-1] * len(nums)
#         stack = []
#         for i in range(len(nums)*2):
#             while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):
#                     dp[stack[-1]] = nums[i%len(nums)]
#                     stack.pop()
#             stack.append(i%len(nums))
#         return dp