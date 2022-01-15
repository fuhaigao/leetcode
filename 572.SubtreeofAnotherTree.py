# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.compare(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
    
    def compare(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.compare(left.left, right.left) and self.compare(left.right, right.right)