class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dic = {}
    #     for i in range(len(nums)):
    #         if nums[i] < 0 or nums[i] > n+1:
    #             nums[i] = n+2
    #         else:
    #             dic[nums[i]] = 1
    #     for i in range(1, n+2):
    #         if i not in dic.keys():
    #             return i
    #     return n+2
    
    #优化
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+1
        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            if nums[val-1] > 0:
                nums[val-1] = -1 * nums[val-1]
            
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1