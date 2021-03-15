# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.helper(res, targetSum, root, [])
        return res

    def helper(self, res, target, root, curr):
        if not root:
            return
        if not root.left and not root.right and target == root.val:
            res.append(curr+[root.val])
            return
        self.helper(res, target-root.val, root.left, curr+[root.val])
        self.helper(res, target-root.val, root.right, curr+[root.val])
