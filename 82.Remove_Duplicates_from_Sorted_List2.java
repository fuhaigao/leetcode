/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head ==  null || head.next == null) return head;
        ListNode dummy = new ListNode(0 == head.val ? 1 : 0);
        // dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;
        ListNode res = dummy;
        while (curr != null && curr.next != null) {
            if (prev.val != curr.val && curr.val != curr.next.val){
                res.next = curr;
                res = res.next;
            }
            prev = curr;
            curr = curr.next;
        }
        if (prev.val != curr.val){
            res.next = curr;
            res = res.next;
        }
        res.next = null;
        return dummy.next;
    }
    
    // my own method:
    // public ListNode deleteDuplicates(ListNode head) {
    //     if (head ==  null || head.next == null) return head;
    //     ListNode dummy = new ListNode(0);
    //     ListNode curr = dummy;
    //     boolean duplicate = false;
    //     while (head != null && head.next != null) {
    //         if (head.val != head.next.val && !duplicate) {
    //             curr.next = head;
    //             curr = curr.next;
    //         }
    //         else if (head.val != head.next.val) duplicate = false;
    //         else duplicate = true;
    //         head = head.next;
    //     }
    //     if (!duplicate){
    //         curr.next=head;
    //         curr = curr.next;
    //     }
    //     curr.next = null;
    //     return dummy.next;
    // }
    
}
