class Solution:
    '''
    stack 
    '''
    def scoreOfParentheses(self, s: str) -> int:
        scores = []
        currScore = 0
        for c in s:
            if c == '(':
                scores.append(currScore)
                currScore = 0
            else:
                currScore = scores.pop() + max(2*currScore, 1)
        return currScore
                