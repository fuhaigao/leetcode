class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.res = []
        self.backtracking(word, "", 0, 0)
        return self.res
    
    def backtracking(self, word, curr, pos, count):
        if pos == len(word):
            if count > 0:
                curr += str(count)
            self.res.append(curr)
            return
        # option 1 skip word and add count
        self.backtracking(word, curr, pos+1, count+1)
        # option 2 include word and clear count
        if count > 0:
            self.backtracking(word, curr+str(count)+word[pos], pos+1, 0)
        else:
            self.backtracking(word, curr+word[pos], pos+1, 0)