# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int: 
        self.traverse(root)
        return self.result
    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        currMax = max(root.val+left, root.val+right, root.val)
        self.result = max(self.result, currMax, root.val+left+right)
        return currMax