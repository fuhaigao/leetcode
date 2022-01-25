class Solution:
    '''
    单调栈
    maintain stack with increasing values, stack[i] = sum of nums[0:i]
    sums[i] - sums[j] >= k meaning  sum(nums[j:i]) >= k
    '''
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        sums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            sums[i+1] = sums[i] + nums[i]
        stack = []
        result = float('inf')
        for i in range(len(nums)+1):
            currSum = sums[i]
            while stack and currSum - sums[stack[0]] >= k:
                length = i - stack.pop(0)
                result = min(result, length)
            while stack and currSum < sums[stack[-1]]:
                stack.pop()
            stack.append(i)
        return result if result != float('inf') else -1

# Cleaner solution 
# class Solution:        
#     def shortestSubarray(self, nums, k):
#         N = len(nums)
#         B = [0] * (N + 1)
#         for i in range(N): 
#             B[i + 1] = B[i] + nums[i]
#         d = []
#         res = N + 1
#         for i in range(N + 1):
#             while d and B[i] - B[d[0]] >= k: 
#                 res = min(res, i - d.pop(0))
#             while d and B[i] <= B[d[-1]]: 
#                 d.pop()
#             d.append(i)
#         return res if res <= N else -1