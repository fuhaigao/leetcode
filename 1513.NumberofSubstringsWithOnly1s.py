class Solution:
    def numSub(self, s: str) -> int:
        res, count = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count = 0
            res += count
        return res % (10**9 + 7)