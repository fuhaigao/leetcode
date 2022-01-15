# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 也可以用recursion，但感觉level order traversal好理解
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue_ = [root]
        depth = 0
        while queue_:
            length = len(queue_)
            depth += 1
            for i in range(length):
                cur = queue_.pop(0)
                if not cur.left and not cur.right:
                    return depth
                if cur.left: queue_.append(cur.left)
                if cur.right: queue_.append(cur.right)

        return depth