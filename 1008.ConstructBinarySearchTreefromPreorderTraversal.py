# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.traverse(preorder[::-1], float('inf'))
    
    def traverse(self, preorder, bound):
        if not preorder or preorder[-1]> bound:
            return None
        root = TreeNode(preorder.pop())
        root.left = self.traverse(preorder, root.val)
        root.right = self.traverse(preorder, bound)
        return root