# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.d = collections.defaultdict(int)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.postOrder(root)
        return self.res

    def postOrder(self, root):
        if not root:
            return "#"
        curr = str(root.val) + "," + self.postOrder(root.left) + \
            self.postOrder(root.right)
        self.d[curr] += 1
        if self.d[curr] == 2:
            self.res.append(root)
        return curr
