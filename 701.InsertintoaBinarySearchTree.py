# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 优化后的结果
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root

# streight forward solution
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)
#         self.helper(root, val)
#         return root
#     def helper(self, root, val):
#         if val < root.val and root.left == None:
#             root.left = TreeNode(val)
#         elif val > root.val and root.right == None:
#             root.right = TreeNode(val)
#         elif val < root.val:
#             self.helper(root.left, val)
#         elif val > root.val:
#             self.helper(root.right, val)
#         return