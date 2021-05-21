# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [root]
        index = 0
        while nodes[index]:
            root = nodes[index]
            nodes.append(root.left)
            nodes.append(root.right)
            index += 1
        while index < len(nodes):
            if nodes[index]:
                return False
            index += 1
        return True