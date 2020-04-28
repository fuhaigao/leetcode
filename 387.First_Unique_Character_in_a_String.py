class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1
        for i, c in enumerate(s):
            if count[ord(c)-ord('a')] == 1:
                return i
        return -1