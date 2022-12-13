# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        self.dfs(root, 0, root.val)
        return self.maximum
    
    #top-bot
    def dfs(self, root, currLength, target):
        if not root:
            return
        if target == root.val:
            currLength += 1
        else:
            currLength = 1
        self.maximum = max(self.maximum, currLength)
        self.dfs(root.left, currLength, root.val+1)
        self.dfs(root.right, currLength, root.val+1)
    
    # bot-up
#     def dfs(self, root):
#         if not root:
#             return 0
#         left = self.dfs(root.left)
#         right = self.dfs(root.right)
#         if left != 0 and root.val == root.left.val-1:
#             left += 1
#         else:
#             left = 0
#         if right !=0 and root.val == root.right.val-1:
#             right += 1
#         else:
#             right = 0
        
#         currLength = max(left, right, 1)
#         self.maximum = max(self.maximum, currLength)
#         return currLength