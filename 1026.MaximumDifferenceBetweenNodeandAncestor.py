# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # The max difference will be maximum - minimum at each leave node, where mx and mn are determined based on nodes from root to leave
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.findMaxDiff(root, root.val, root.val)
    def findMaxDiff(self, root, mx, mn):
        if not root:
            return mx - mn
        mx = max(mx, root.val)
        mn = min(mn, root.val)
        return max(self.findMaxDiff(root.left, mx, mn), self.findMaxDiff(root.right, mx, mn))