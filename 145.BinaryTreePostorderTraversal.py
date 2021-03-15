# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while root or stack:
            if root:
                stack.append(root)
                res.insert(0,root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return res
        