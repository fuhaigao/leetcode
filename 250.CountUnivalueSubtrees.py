# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.dfs(root)
        return self.total
    
    def dfs(self, root):
        if not root:
            return True
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left and right:
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False
            self.total += 1
            return True

        return False
