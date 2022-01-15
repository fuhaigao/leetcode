# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    重点在于先思考traversal顺序，然后如何accumulate sum
    '''
    currSum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.right = self.convertBST(root.right)
        root.val += self.currSum
        self.currSum = root.val
        root.left = self.convertBST(root.left)
        return root