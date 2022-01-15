# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        因为stack FILO，所以要先 push right，再push left。 这样 pop 的顺序就是先left再right
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return result