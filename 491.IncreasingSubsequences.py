class Solution:
    '''
    重点：因为不能排序修改nums，所以不能用之前的去重方法
    要在每个for loop中，创建一个新的set visited存加过的数
    '''
    def __init__(self):
        self.res = []
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0, [])
        return self.res
    def backtracking(self, nums, index, path):
        if len(path) >= 2:
            self.res.append(path)
        visited = set()
        for i in range(index, len(nums)):
            if (len(path)>0 and nums[i] < path[-1]) or (nums[i] in visited):
                continue
            visited.add(nums[i])
            self.backtracking(nums, i+1, path+[nums[i]])