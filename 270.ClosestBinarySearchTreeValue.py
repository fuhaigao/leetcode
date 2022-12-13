# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        minDiff, res = float('inf'), 0
        while root:
            diff = abs(root.val - target)
            if diff < minDiff:
                minDiff = diff
                res = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return res
