# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key == root.val:
            if root.left == None and root.right == None:
                return None
            if root.left and root.right == None:
                return root.left
            if root.right and root.left == None:
                return root.right
            else:
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                return root.right
        root.left = self.deleteNode(root.left, key)
        root. right = self.deleteNode(root.right, key)
        return root
            