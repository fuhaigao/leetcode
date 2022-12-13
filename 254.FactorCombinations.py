class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.res = []
        self.backtracking(n, [], 2)
        return self.res
    def backtracking(self, n, curr, start):
        if n <= 1: 
            if len(curr) > 1:
                self.res.append(curr)
            return
        for num in range(start, math.isqrt(n)+1):
            if n%num == 0:
                self.backtracking(n//num, curr+[num], num)
        self.backtracking(n//n, curr+[n], n)