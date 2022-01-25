class Solution:
    def __init__(self):
        self.result = 0
    def countArrangement(self, n: int) -> int:
        used = [0]*(n+1)
        self.backtracking(1, used, n)
        return self.result
    
    def backtracking(self, pos, used, n):
        if pos > n:
            self.result += 1
            return
        for i in range(1, n+1):
            if used[i]==0 and (pos%i == 0 or i%pos == 0):
                used[i] = 1
                self.backtracking(pos+1, used, n)
                used[i] = 0
        