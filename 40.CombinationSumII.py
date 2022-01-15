class Solution:
    def __init__(self):
        self.res =[]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking([], target, 0, candidates)
        return self.res
    def backtracking(self, path, target, index, candidates):
        if target == 0:
            self.res.append(path)
        else:
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] <= target:
                    self.backtracking(path+[candidates[i]], target-candidates[i], i+1, candidates)
        return