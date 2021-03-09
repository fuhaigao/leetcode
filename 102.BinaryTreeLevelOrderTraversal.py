# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while (queue):
            size = len(queue)
            tmp = []
            for i in range(size):
                curr_node = queue.pop(0)
                tmp.append(curr_node.val)
                if (curr_node.left != None):
                    queue.append(curr_node.left)
                if (curr_node.right != None):
                    queue.append(curr_node.right)
            res.append(tmp)
        return res
                
        