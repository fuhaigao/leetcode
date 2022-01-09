class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if self.isStretchy(s, word):
                count += 1
        return count
    
    def isStretchy(self, s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                len_s = self.getRepeatedLength(s, i)
                len_word = self.getRepeatedLength(word, j)
                if (len_s != len_word and len_s < 3) or len_s < len_word:
                    return False
                i += len_s
                j += len_word
            else:
                return False
        return i == len(s) and j == len(word)
    
    def getRepeatedLength(self, s, index):
        end = index
        while end < len(s) and s[end] == s[index]:
            end += 1
        return end - index