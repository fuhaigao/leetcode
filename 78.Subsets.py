class Solution:
    def __init__(self):
        self.res = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0, [])
        return self.res
    def backtracking(self, nums, index, path):
        self.res.append(path)
        if index < len(nums):
            for i in range(index, len(nums)):
                self.backtracking(nums, i+1, path+[nums[i]])