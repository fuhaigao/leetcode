class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtracking([], k, 1, n, res)
        return res
    def backtracking(self, path, k, index, target, res):
        if target == 0 and len(path) == k:
            res.append(path)
        else:
            for i in range(index, 10):
                if i <= target and len(path)<k:
                    self.backtracking(path+[i], k, i+1, target-i, res)
        return
            