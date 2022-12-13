# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        self.dfs(root)
        return self.maxLength
    
    def dfs(self, root):
        if not root:
            return 0, 0
        incLeft, decLeft = self.dfs(root.left)
        incRight, decRight = self.dfs(root.right)
        
        inc, dec = 1, 1
        if root.left:
            if root.val+1 == root.left.val:
                dec += decLeft
            if root.val == root.left.val+1:
                inc += incLeft
        if root.right:
            if root.val+1 == root.right.val:
                dec = max(dec, 1+decRight)
            if root.val == root.right.val+1:
                inc = max(inc, 1+incRight)
        self.maxLength = max(self.maxLength, inc+dec-1)
        return inc, dec