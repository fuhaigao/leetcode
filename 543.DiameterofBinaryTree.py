# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maximum = [0]
        self.helper(maximum, root)
        return maximum[0]
    def helper(self, maximum, root):
        if not root:
            return 0
        l = self.helper(maximum, root.left)
        r = self.helper(maximum, root.right)
        maximum[0] = max(maximum[0], l+r)
        return 1 + max(l, r)