class Solution:
    def __init__(self):
        self.res = []
        self.target = 0
    def addOperators(self, num: str, target: int) -> List[str]:
        self.target = target
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return self.res
            
    def dfs(self, num, currStr, currVal, last):
        if len(num) == 0:
            if currVal == self.target:
                self.res.append(currStr)
            return
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                curr = num[:i]
                self.dfs(num[i:], currStr+"+"+curr, currVal+int(curr), int(curr))
                self.dfs(num[i:], currStr+"-"+curr, currVal-int(curr), -int(curr))
                self.dfs(num[i:], currStr+"*"+curr, currVal-last+last*int(curr), last*int(curr))