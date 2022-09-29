class Solution:
    def checkRecord(self, s: str) -> bool:
        # numAbsent = 0
        # numLate = 0
        # for c in s:
        #     if c == 'A':
        #         numAbsent += 1
        #         numLate = 0
        #     elif c == 'L':
        #         numLate += 1
        #     else:
        #         numLate = 0
        #     if numAbsent == 2 or numLate == 3:
        #         return False
        # return True
        return s.count('A') <= 1 and s.count('LLL') == 0
