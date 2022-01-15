# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 也可以用 level order traversal 
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        count = 1
        count += self.countNodes(root.left)
        count += self.countNodes(root.right)
        return count