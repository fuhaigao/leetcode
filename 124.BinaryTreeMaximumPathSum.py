# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # use arr to pass maximum by reference
        maximum = [-sys.maxsize]
        self.helper(root, maximum)
        return maximum[0]

    def helper(self, root, maximum):
        if not root:
            return 0
        left = max(self.helper(root.left, maximum), 0)
        right = max(self.helper(root.right, maximum), 0)
        maximum[0] = max(maximum[0], root.val + left +right)
        return root.val + max(left, right)