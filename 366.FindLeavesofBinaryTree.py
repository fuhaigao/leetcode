# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = collections.defaultdict(list)
        
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root)
        res = []
        for depth, nodes in sorted(self.nodes.items()):
            res.append(nodes)
        return res
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        depth = max(left, right) + 1
        self.nodes[depth].append(root.val)
        return depth