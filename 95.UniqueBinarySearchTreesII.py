# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        res = self.backtracking(1, n)
        return res
    def backtracking(self, start, end):
        if start > end:
            return [None]
        curr = []
        for root in range(start, end+1):
            left = self.backtracking(start, root-1)
            right = self.backtracking(root+1, end)
            for leftNode in left:
                for rightNode in right:
                    rootNode = TreeNode(root)
                    rootNode.left = leftNode
                    rootNode.right = rightNode
                    curr.append(rootNode)
        return curr