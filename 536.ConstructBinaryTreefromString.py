# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isnumeric() or s[i] == '-':
                j = i
                while j+1<len(s) and s[j+1].isnumeric():
                    j += 1
                currNode = TreeNode(int(s[i:j+1]))
                i = j
                if stack:
                    parentNode = stack[-1]
                    if parentNode.left:
                        parentNode.right = currNode
                    else:
                        parentNode.left = currNode
                stack.append(currNode)
            elif s[i] == ')':
                stack.pop()
            i += 1
        return stack[0] if stack else None
                