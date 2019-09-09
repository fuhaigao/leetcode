/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// swap nodes 基础
// main logics in while loop
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode l1 = dummy;
        ListNode l2 = head;
        dummy.next = head;
        while (l2 != null && l2.next != null){
            // Ex. 1, 2, 3, 4
            //l1 = pointer before 1. l2 = porinter at 1
            ListNode nextStart = l2.next.next;
            l1.next = l2.next;
            l2.next.next = l2;
            l2.next = nextStart;
            l1 = l2;
            l2 = l2.next;
        }
        return dummy.next;
    }
}
