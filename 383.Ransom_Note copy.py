class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1,10):
            self.dfs(res, i, n)
        return res
    
    def dfs(self, res, curr, n):
        if curr > n:
            return
        res.append(curr)
        for i in range(10):
            self.dfs(res, curr*10+i, n)
        return