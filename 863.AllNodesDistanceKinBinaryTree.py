# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
1. Find the node with val == target with postorder traversal. While traversing, record the distance to the target for each node in the same subtree.
e.g.
    1
  2   3
4  5 6  7 

if target = 4, only subtree (1,2) can store the distance to target

2. Then use Preorder traversal to calculate the distance to the target. Update distance to stored value if the node is in dictionary.
e.g. distance for node 1 will be 2, so distance for node 3 will become 2+1=3

'''
class Solution:
    def __init__(self):
        self.nodeToDist = dict()
        self.result = []
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dist = self.find(root, target)
        self.traverse(root, 0, k)
        return self.result
    
    def find(self, root, target):
        if not root:
            return -1
        if root == target:
            self.nodeToDist[root] = 0
            return 0
        left = self.find(root.left, target)
        if left >= 0:
            self.nodeToDist[root] = left+1
            return left+1
        right = self.find(root.right, target)
        if right >= 0:
            self.nodeToDist[root] = right+1
            return right+1
        return -1
    
    def traverse(self, root, dist, k):
        if not root:
            return
        if root in self.nodeToDist:
            dist = self.nodeToDist[root]
        if dist == k:
            self.result.append(root.val)
        self.traverse(root.left, dist+1, k)
        self.traverse(root.right, dist+1, k)