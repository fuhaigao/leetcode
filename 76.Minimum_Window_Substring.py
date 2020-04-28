class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict = {}
        count = len(t)
        for c in t:
            dict[c] = dict.get(c, 0) + 1
        begin, end, head = 0, 0, 0
        min_length = float('inf')
        
        while end < len(s):
            cEnd = s[end]
            dict[cEnd] = dict.get(cEnd, 0)-1
            if dict[cEnd] >= 0:
                count -= 1
            end += 1
            
            while count == 0:
                if end-begin < min_length:
                    min_length = end-begin
                    head = begin
                cBegin = s[begin]
                if dict[cBegin] == 0:
                    count += 1
                dict[cBegin] += 1
                begin += 1
                
        if min_length == float('inf'):
            return ""
        else:
            return s[head: head+min_length]