/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;
        ListNode curr = head;
        int size = 1;
        while (curr.next!=null ){
            curr = curr.next;
            size++;
        }
        curr.next = head;
        for (int i=0; i<size-k%size; i++){
            curr =curr.next;
        }
        head = curr.next;
        curr.next = null;
        return head;
    }
}
