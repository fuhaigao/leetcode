class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        slist = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    slist[i] = ''
        
        while stack:
            slist[stack.pop()] = ''
        return ''.join(slist)