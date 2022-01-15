# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    BST保证inorder traversal的数是从大到小排列的
    '''
    count = 0
    result = []
    prev = -1
    maxCount = 0
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.result
            
    def traversal(self, root):
        if not root:
            return
        self.traversal(root.left)
        if self.prev == root.val:
            self.count += 1
        else:
            self.count = 1
        if self.count == self.maxCount:
            self.result.append(root.val)
        if self.count > self.maxCount:
            self.maxCount = self.count
            self.result.clear()
            self.result.append(root.val)
        self.prev = root.val
        self.traversal(root.right)