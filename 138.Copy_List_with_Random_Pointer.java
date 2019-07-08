/*
 // Definition for a Node.
 class Node {
 public int val;
 public Node next;
 public Node random;
 
 public Node() {}
 
 public Node(int _val,Node _next,Node _random) {
 val = _val;
 next = _next;
 random = _random;
 }
 };
 */
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        // 1st Step: Make copy of each node
        // and link them together side-by-side in a single list.
        Node curr = head;
        while (curr != null) {
            Node next = curr.next;
            Node copy = new Node(curr.val);
            curr.next = copy;
            curr.next.next = next;
            curr = next;
        }
        
        // 2nd Step: assign random pointers for the copy nodes.
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }
        
        // 3rd Step: restore the original list, and extract the copy list.
        curr = head;
        Node copyHead = head.next;      // for future return
        Node copy = copyHead;           // for future iteration and set next node
        while (copy.next != null) {
            curr.next = curr.next.next;
            curr = curr.next;
            
            copy.next = copy.next.next;
            copy = copy.next;
        }
        curr.next = null;
        return copyHead;
    }
}
