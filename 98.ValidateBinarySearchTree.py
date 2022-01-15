# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = list()
        self.traversal(root, nums)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True
    
    def traversal(self, root, nums):
        if not root:
            return
        self.traversal(root.left, nums)
        nums.append(root.val)
        self.traversal(root.right, nums)