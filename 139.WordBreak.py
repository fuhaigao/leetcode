class Solution:
    '''
    dp[i]: true/false until the ith character in s
    transform function: dp[i] = dp[i] or (dp[j] and s[j:i] in wordDict)
        - 如果s[j:i]存在dict中，并且dp[j]==True（s[0:j]也满足分割条件）, 那么dp[i] 也满足分割条件
    init: dp[0] = True, other False
    traversal: two-loop 
        1. traverse s: range(0, len(s)+1)
        2. traverse sub-string range(0, i)
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                dp[i] = dp[i] or (dp[j] and self.checkDict(s[j: i], wordDict))
        return dp[n]
    
    def checkDict(self, s, wordDict):
        if s in wordDict:
            return True
        return False