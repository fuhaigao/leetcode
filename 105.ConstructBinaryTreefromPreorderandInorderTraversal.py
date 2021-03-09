# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        res = self.helper(preorder, inorder, 0, 0, len(inorder)-1)
        return res

    def helper(self, preorder, inorder, preStart, inStart, inEnd):
        # end condition
        if preStart >= len(preorder) or inStart > inEnd:
            return None

        rootVal = preorder[preStart]
        curr = TreeNode(rootVal)
        inIndex = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                inIndex = i
                break

        curr.left = self.helper(preorder, inorder, preStart+1, inStart, inIndex-1)
        # right index = preorder + num_leftNodes = preorder + (inIndex - inStart)
        curr.right = self.helper(preorder, inorder, preStart+(inIndex-inStart+1), inIndex+1, inEnd)
        return curr