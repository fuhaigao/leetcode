class Solution:
    def canWin(self, currentState: str) -> bool:
        return self.backtracking(currentState)
    
    def backtracking(self, s):
        for i in range(1, len(s)):
            if s[i-1] == "+" and s[i] == "+":
                canwin = self.backtracking(s[:i-1] +"--"+ s[i+1:])
                if canwin == False:
                    return True
        return False