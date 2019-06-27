/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode tmp = new ListNode(0);
        for (int i=0; i<m-1; i++) {
            prev = prev.next;
        }
        ListNode curr = prev.next;
        for (int i=0; i<n-m; i++) {
            tmp = prev.next;
            prev.next = curr.next;
            curr.next = curr.next.next;
            prev.next.next =tmp;
        }
        return dummy.next;
    }
}
