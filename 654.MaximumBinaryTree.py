# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, start, end):
        if start > end:
            return None
        maxValue = float('-inf')
        maxIndex = 0
        for i in range(start, end+1):
            if nums[i] > maxValue:
                maxValue = nums[i]
                maxIndex = i
        root = TreeNode(maxValue)
        root.left = self.helper(nums, start, maxIndex-1)
        root.right = self.helper(nums, maxIndex+1, end)
        return root
    
# Method 2: 优化
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
#         maxvalue = max(nums)
#         index = nums.index(maxvalue)
        
#         root = TreeNode(maxvalue)

#         left = nums[:index]
#         right = nums[index + 1:]

#         root.left = self.constructMaximumBinaryTree(left)
#         root.right = self.constructMaximumBinaryTree(right)
#         return root
        