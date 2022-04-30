class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        missedLetter = len(t)
        minLength = float('inf')
        left, pos = 0, 0
        minStart = -1
        # for c in t:
        #     counter[c] += 1
        while pos < len(s):
            counter[s[pos]] -= 1
            if counter[s[pos]] >= 0:
                missedLetter -= 1
            while missedLetter == 0:
                currLength = pos-left+1
                if currLength < minLength:
                    minLength = currLength
                    minStart = left
                counter[s[left]] += 1
                if counter[s[left]] > 0:
                    missedLetter += 1
                left += 1
            pos += 1
        return s[minStart:minStart+minLength] if minStart != -1 else ""
