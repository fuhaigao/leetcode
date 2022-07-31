# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)
    
    def traverse(self, root, value):
        curr = value << 1 | root.val
        if root.left and root.right:
            return self.traverse(root.left, curr) + self.traverse(root.right, curr)
        if root.left:
            return self.traverse(root.left, curr)
        if root.right:
            return self.traverse(root.right, curr)
        return curr