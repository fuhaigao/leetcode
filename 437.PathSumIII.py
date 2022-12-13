# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        self.dfs(root, targetSum, cache, 0)
        return self.res
        
    def dfs(self, root, target, cache, currSum):
        if not root:
            return
        currSum += root.val
        oldSum = currSum - target
        self.res += cache[oldSum]
        cache[currSum] += 1
        self.dfs(root.left, target, cache, currSum)
        self.dfs(root.right, target, cache, currSum)
        cache[currSum] -= 1