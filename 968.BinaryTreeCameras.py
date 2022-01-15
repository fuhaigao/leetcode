# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    https://programmercarl.com/0968.%E7%9B%91%E6%8E%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
    Three situation
    0. not covered by camera
    1. has camera
    2. coverd by camera
    '''
    count = 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if self.helper(root) == 0:
            self.count += 1
        return self.count
    
    def helper(self, root):
        if root == None:
            return 2
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left == 2 and right == 2:
            return 0
        if left == 0 or right == 0:
            self.count += 1
            return 1
        elif left == 1 or right == 1:
            return 2
        # else:
        #     return 0