class Solution:
    def __init__(self):
        self.res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking([], target, 0, candidates)
        return self.res
        
    def backtracking(self, path, target, index, candidates):
        if target == 0:
            self.res.append(path)
        else:
            for i in range(index, len(candidates)):
                if candidates[i] <= target:
                    self.backtracking(path+[candidates[i]], target-candidates[i], i, candidates)
        return