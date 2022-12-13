# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        colToNodes = collections.defaultdict(list)
        queue = collections.deque([(0, root)])
        
        while queue:
            col, node = queue.popleft()
            colToNodes[col].append(node.val)
            if node.left:
                queue.append((col-1, node.left))
            if node.right:
                queue.append((col+1, node.right))
        
        res = []
        for _, vals in sorted(colToNodes.items()):
            res.append(vals)
        return res