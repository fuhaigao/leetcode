# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = TreeNode(float("-inf"))
    first, second = TreeNode(float("-inf")), TreeNode(float("-inf"))
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return
    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if self.first.val == float("-inf") and self.pre.val > root.val:
            self.first = self.pre
        if self.first.val != float("-inf") and self.pre.val > root.val:
            self.second = root
        self.pre = root
        self.inorder(root.right)
        return