class Solution:
    # recursion
    # def minDistance(self, word1: str, word2: str) -> int:
    #     if not word1 and not word2:
    #         return 0
    #     if not word1:
    #         return len(word2)
    #     if not word2:
    #         return len(word1)
    #     if word1[0] == word2[0]:
    #         return self.minDistance(word1[1:], word2[1:])
    #     insert = 1 + self.minDistance(word1, word2[1:])
    #     delete = 1 + self.minDistance(word1[1:], word2)
    #     update = 1 + self.minDistance(word1[1:], word2[1:])
    #     return min(insert, min(delete, update))
    
    # dp
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
        return dp[m][n]