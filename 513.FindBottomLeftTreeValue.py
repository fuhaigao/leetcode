# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDepth = float('-inf')
    result = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(0, root)
        return self.result
    def dfs(self, depth, node):
        if node == None:
            return
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.result = node.val
        self.dfs(depth+1, node.left)
        self.dfs(depth+1, node.right)