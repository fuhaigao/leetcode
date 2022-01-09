class Solution:
    # dp: 背包问题
    def numSquares(self, n: int) -> int:
        results = [float('inf')]*(n+1)
        results[0] = 0
        for i in range(1, n+1):
            curr = 1
            while curr*curr <= i:
                results[i] = min(results[i], results[i-curr*curr]+1)
                curr += 1
        return results[n]