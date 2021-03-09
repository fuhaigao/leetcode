class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '[': ']', '{': '}'}
        for c in s:
            if c in dic.keys():
                stack.append(dic[c])
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False
        return True if len(stack) == 0 else False