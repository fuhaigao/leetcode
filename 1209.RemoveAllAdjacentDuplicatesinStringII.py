class Solution:
    '''
    Simple and Easy but hard to get the clean and clear idea at first glance
    '''
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  #stores (c, frequency)
        for c in s:
            if len(stack) > 0 and stack[-1][0] == c:
                 stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()
        result = ""
        for item in stack:
            result += item[1]*item[0]
        return result