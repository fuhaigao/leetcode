class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict, index, end, count, minLength = {}, 0, 0, len(t), sys.maxsize
        minStart = 0
        for c in t:
            dict[c] = dict.get(c, 0)+1
        
        while end < len(s):
            currChar = s[end]
            dict[currChar] = dict.get(currChar, 0)-1
            if dict[currChar] >= 0:
                count -= 1
            end += 1

            while count == 0:
                if end-index < minLength:
                    minLength = end-index
                    minStart = index
                dict[s[index]] += 1
                if dict[s[index]] > 0:
                    count += 1
                index += 1
        
        return s[minStart:minStart+minLength] if minLength != sys.maxsize else ""