"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        dummy = Node(0)
        curr = dummy
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            curr.right = node
            node.left = curr
            curr = curr.right
            root = node.right
        head = dummy.right
        head.left = curr
        curr.right = head
        return head
    
# Divid and Conquer Solution
# public Node treeToDoublyList(Node root) {
#         if(root==null) return root;
        
#         Node lh=treeToDoublyList(root.left);
#         Node rh=treeToDoublyList(root.right);
#         Node rt=null;
        
#         if(lh!=null) {
#             lh.left.right=root;
#             root.left=lh.left;
#         } else {
#             lh=root;
#         }
        
#         if(rh!=null) {
#             rt=rh.left;
#             rh.left=root;
#             root.right=rh;
#         } else {
#             rt=root;
#         }
        
#         lh.left=rt;
#         rt.right=lh;
        
#         return lh;
        
# }