class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for numDistinct in range(1, 27):
            res = max(res, self.findLongestDistinct(s, k, numDistinct))
        return res
    
    def findLongestDistinct(self, s, k, numDistinct):
        begin, end = 0, 0
        uniqueNum, noLessThanKNum = 0, 0
        count = {}
        max_length = 0
        # Two pointer sliding window
        while end < len(s):
            cEnd = s[end]
            count[cEnd] = count.get(cEnd, 0) + 1
            if count[cEnd] == 1:
                uniqueNum += 1
            if count[cEnd] == k:
                noLessThanKNum += 1
            end += 1
            
            while uniqueNum > numDistinct:
                cBegin = s[begin]
                if count[cBegin] == 1:
                    uniqueNum -= 1
                if count[cBegin] == k:
                    noLessThanKNum -= 1
                count[cBegin] = count[cBegin] - 1
                begin += 1
            if uniqueNum == noLessThanKNum:
                max_length = max(max_length, end-begin)
        return max_length
                