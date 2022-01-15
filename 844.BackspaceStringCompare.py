class Solution:
    # Two pointer
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        sBack, tBack = 0, 0
        while i>=0 or j>=0:
            while i >= 0 and (s[i]=='#' or sBack != 0):
                if s[i] == '#':
                    sBack += 1
                else:
                    sBack -= 1
                i -= 1
            while j >= 0 and (t[j]=='#' or tBack != 0):
                if t[j] == '#':
                    tBack += 1
                else:
                    tBack -= 1
                j -= 1
            if (i<0 and j>=0) or (i>=0 and j<0):
                return False
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True