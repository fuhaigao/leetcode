class Solution:
    '''
    backtracking, but maybe can be optimized by dp
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        
        def dfs(index, path):
            if index == len(s):
                res.append(" ".join(path))
                return
            for i in range(index, len(s)):
                if s[index:i+1] in wordDict:
                    dfs(i+1, path + [s[index:i+1]])
        dfs(0, [])
        return res