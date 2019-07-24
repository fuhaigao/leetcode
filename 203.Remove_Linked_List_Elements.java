/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while (head != null){
            if (head.val != val){
                prev.next = head;
                prev = prev.next;
            }
            head = head.next;
        }
        prev.next = null;
        return dummy.next;
    }
}
