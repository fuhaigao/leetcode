class Solution:
    def calculate(self, s: str) -> int:
        curr, res, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                curr = curr*10 + int(c)
            elif c == '+':
                res += sign * curr
                curr = 0
                sign = 1
            elif c == '-':
                res += sign * curr
                curr = 0
                sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * curr
                res *= stack.pop()
                res += stack.pop()
                curr = 0
                sign = 1
        if curr:
            res += sign * curr
        return res