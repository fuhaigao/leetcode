# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.frequency = collections.defaultdict(int)
        
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        maxOccurence = 0
        result = []
        for key in self.frequency:
            if self.frequency[key] > maxOccurence:
                maxOccurence = self.frequency[key]
                result.clear()
                result.append(key)
            elif self.frequency[key] == maxOccurence:
                result.append(key)
        return result
    
    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        curr = left + right + root.val
        self.frequency[curr] += 1
        return curr