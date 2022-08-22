class Solution:
    def __init__(self):
        self.res = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.backtracking(0, 0, "", n)
        return self.res
    def backtracking(self, left, right, path, n):
        if left == right and right == n:
            self.res.append(path)
        if left < n:
            self.backtracking(left+1, right, path+"(", n)
        if right < left:
            self.backtracking(left, right+1, path+")", n)