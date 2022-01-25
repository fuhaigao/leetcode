class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        result = 0
        for c in s:
            if c =='(':
                count += 1
            if c ==')':
                count -= 1
            if count < 0:
                count += 1
                result += 1
        return result + count