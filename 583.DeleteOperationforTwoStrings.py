class Solution:
    '''
    dp[i][j]: number of steps that make word1[0:i] == word2[0:j]
    transform function:
        if word1[i] == word2[j]:
            dp[i+1][j+1] = dp[i][j]
        else:
            dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1])+1
    https://programmercarl.com/0583.%E4%B8%A4%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%88%A0%E9%99%A4%E6%93%8D%E4%BD%9C.html#%E6%80%9D%E8%B7%AF
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = i
        for i in range(n2+1):
            dp[0][i] = i
        for i in range(n1):
            for j in range(n2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j]+2)
        return dp[-1][-1]