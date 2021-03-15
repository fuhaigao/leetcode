class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        maximum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    maximum = max(maximum, dp[i+1][j+1])
        return maximum*maximum