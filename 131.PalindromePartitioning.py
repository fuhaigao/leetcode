class Solution:
    def __init__(self):
        self.res =[]
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking([], s)
        return self.res
    def backtracking(self, path, s):
        if len(s) == 0:
            self.res.append(path)
        for i in range(len(s)):
            currStr = s[0:i+1]
            if self.isPalindrome(currStr):
                self.backtracking(path+[currStr], s[i+1:])
        return
        
    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True