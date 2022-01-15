# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Inorder traversal ensures the value increase from smallest to largest
    Just find the minDifference between any two neighbour numbers
    '''
    prev = float('inf')
    minDifference = float('inf')
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.minDifference
    
    def traversal(self, root):
        if not root:
            return
        self.traversal(root.left)
        difference = abs(root.val - self.prev)
        self.minDifference = min(self.minDifference, difference)
        self.prev = root.val
        self.traversal(root.right)