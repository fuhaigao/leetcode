class Solution:
    def __init__(self):
        self.res = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, 0, [])
        return self.res
    
    def backtracking(self, nums, index, path):
        self.res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.backtracking(nums, i+1, path+[nums[i]])