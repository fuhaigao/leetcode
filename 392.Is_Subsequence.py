class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        indexS, indexT = 0,0
        while indexT < len(t):
            if s[indexS] == t[indexT]:
                indexS += 1
                if indexS == len(s):
                    return True
            indexT += 1
        return False