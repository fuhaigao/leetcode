# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Not very clean, but idea is recursively build tree
    def __init__(self):
        self.traversal = ""
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.traversal = traversal
        return self.buildTree(0)
    
    def buildTree(self, depth):
        dashCount = 0
        for s in self.traversal:
            if s != '-':
                break
            dashCount += 1
        if dashCount == depth:
            self.traversal = self.traversal[depth:]
            val = self.getNumber()
            root = TreeNode(val)
            root.left = self.buildTree(depth+1)
            root.right = self.buildTree(depth+1)
            return root
        return None
    
    def getNumber(self):
        i = 0
        num = 0
        while i<len(self.traversal) and self.traversal[i].isdigit():
            num = num*10 + int(self.traversal[i])
            i += 1
        self.traversal = self.traversal[i:]
        return num
