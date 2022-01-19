class Solution:
    '''
    dp[i][j]: the number of subsequence s[0:i] has that is equal to t[0:j]
    transform function: 
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i][j+1]
    https://programmercarl.com/0115.%E4%B8%8D%E5%90%8C%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.html#%E6%80%9D%E8%B7%AF
    '''
    def numDistinct(self, s: str, t: str) -> int:
        lenS, lenT = len(s), len(t)
        dp = [[0]*(lenT+1) for i in range(lenS+1)]
        for i in range(lenS+1):
            dp[i][0] = 1
        for i in range(lenS):
            for j in range(lenT):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]