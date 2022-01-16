class Solution:
    '''
    1. dp数组: dp[i][j] = largest number of subset at i个0 & j个1
    2. transfermation function: dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
    3. 遍历顺序: i从大到小, j从大到小
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for x in range(m+1)]
        for s in strs:
            ones, zeros = 0, 0
            for c in s:
                if c == '1':
                    ones += 1
                if c == '0':
                    zeros += 1 
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
            # print(dp)
                
        return dp[m][n]