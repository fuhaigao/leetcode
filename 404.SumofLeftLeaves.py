# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    leftLeavesSum = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root, False)
        return self.leftLeavesSum
    def dfs(self, node, isLeft):
        if node.left == None and node.right == None and isLeft:
            self.leftLeavesSum += node.val
            return
        if node.left:
            self.dfs(node.left, True)
        if node.right:
            self.dfs(node.right, False)
        