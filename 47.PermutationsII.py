class Solution:
    '''
    此方法好理解，但占用额外的内存。另一种方法可以看cpp
    '''
    def __init__(self):
        self.res = []
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, [], set())
        return self.res
    
    def backtracking(self, nums, path, visited):
        if len(path) == len(nums):
            self.res.append(path)
        used = set()
        for i in range(len(nums)):
            if i not in visited and nums[i] not in used:
                used.add(nums[i])
                visited.add(i)
                self.backtracking(nums, path+[nums[i]], visited)
                visited.remove(i)