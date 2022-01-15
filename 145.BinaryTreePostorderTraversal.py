# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        区别于preorder，只需要 append替换成insert(0)
        注意：还要改成 先push left 再push right，这样pop的结果就是先右后左，配合insert(0)顺序才对
        *也可以不用insert(0, value), 最后对res进行reverse
    '''
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            res.insert(0, root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res