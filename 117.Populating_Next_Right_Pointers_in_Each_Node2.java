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
        Node head = root;
        Node nextHead = new Node();
        nextHead.next = root;
        while (nextHead.next != null) {
            Node tail = nextHead;       // 为了更新 nextHead.next to next level, 因为 tail = nextHead, 所以 当 tail = curr.left/curr.right 时， nextHead 也会move to next level
            Node curr = nextHead.next;  // 为了copy current level： curr points to current level start
            nextHead.next = null;       // 为了让 previous level 的最后连接null (previous.next = null)
            while (curr != null) {
                if (curr.left != null) {
                    tail.next = curr.left;
                    tail = tail.next;
                }
                if (curr.right != null) {
                    tail.next = curr.right;
                    tail = tail.next;
                }
                curr = curr.next;
            }
        }
        return head;
    }
}
