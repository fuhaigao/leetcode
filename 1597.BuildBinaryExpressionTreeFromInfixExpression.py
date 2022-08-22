# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/discuss/864596/Python-Standard-parser-implementation
    '''
    def expTree(self, s: str) -> 'Node':
        print("1")
        queue = collections.deque(list(s))
        return self.parseAddSub(queue)
    
    def parseAddSub(self, tokens):
        left = self.parseMulDiv(tokens)
        while len(tokens) > 0 and tokens[0] in ["+", "-"]:
            node = Node(val = tokens.popleft())
            node.left = left
            node.right = self.parseMulDiv(tokens)
            left = node
        return left
    
    def parseMulDiv(self, tokens):
        left = self.parseBrackets(tokens)
        while len(tokens) > 0 and tokens[0] in ["*", "/"]:
            node = Node(val = tokens.popleft())
            node.left = left
            node.right = self.parseBrackets(tokens)
            left = node
        return left
        
    def parseBrackets(self, tokens):
        if tokens[0] == '(':
            tokens.popleft()
            node = self.parseAddSub(tokens)
            tokens.popleft()
            return node
        else:
            node = Node(val = tokens.popleft())
            return node