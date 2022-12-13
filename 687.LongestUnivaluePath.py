# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        self.dfs(root)
        return self.maximum
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        leftDepth, rightDepth = 0,0
        if root.left and root.val == root.left.val:
            leftDepth = left
        if root.right and root.val == root.right.val:
            rightDepth = right
        self.maximum = max(self.maximum, leftDepth + rightDepth)
        return max(leftDepth, rightDepth)+1