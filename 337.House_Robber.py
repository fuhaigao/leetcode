# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result = self.traverse(root)
        return max(result)
    
    def traverse(self, root):
        if not root:
            return (0, 0)
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        selectCurrentNode = root.val + left[0] + right[0]
        unselectCurrentNode = max(left) + max(right)
        return (unselectCurrentNode, selectCurrentNode)