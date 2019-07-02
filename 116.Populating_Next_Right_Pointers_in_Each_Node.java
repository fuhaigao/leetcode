/*
 // Definition for a Node.
 class Node {
 public int val;
 public Node left;
 public Node right;
 public Node next;
 
 public Node() {}
 
 public Node(int _val,Node _left,Node _right,Node _next) {
 val = _val;
 left = _left;
 right = _right;
 next = _next;
 }
 };
 */
class Solution {
    public Node connect(Node root) {
        Node head = root;   //for return
        Node curr = new Node();
        while (root != null && root.left != null) {
            curr = root;
            while (curr != null) {
                curr.left.next = curr.right;
                if (curr.next == null) curr.right.next = null;
                else curr.right.next = curr.next.left;
                curr = curr.next;
            }
            root = root.left;
        }
        return head;
    }
}
