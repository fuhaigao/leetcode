class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start, res = -1, 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i
                else:
                    stack.pop()
                    # complete parentheses
                    if len(stack) == 0:
                        res = max(res, i-start)
                    # Have ( not closed
                    else:
                        res = max(res, i-stack[-1])
        return res
                