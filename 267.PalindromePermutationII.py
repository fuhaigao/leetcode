class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        self.res = []
        counter = collections.Counter(s)
        mid = [key for key, val in counter.items() if val%2]
        if len(mid) > 1:
            return []
        self.mid = "" if len(mid) == 0 else mid[0]
        half = ''.join([k * (v//2) for k, v in counter.items()])
        half = [c for c in half]
        self.backtracking("", half)
        return self.res
    
    def backtracking(self, curr, s):
        if len(s) == 0:
            self.res.append(curr+self.mid+curr[::-1])
            return
        
        used = set()
        for i in range(len(s)):
            if s[i] not in used:
                used.add(s[i])
                self.backtracking(curr+s[i], s[:i]+s[i+1:])