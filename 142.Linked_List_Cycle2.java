/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

// https://www.cnblogs.com/wuyuegb2312/p/3183214.html
// prove:
// 设 start 到 cycle_begin 的长度为L， cycle_begin 到 first_meet 为 x, cycyle 总长度为 R
// 当第一次相遇时： slow position: x%R;  fast position: (2*(L+x)-L)%R
// 因为两个position相等 x%R == (L+2x)%R  => (L+x)%R = 0
// (2L+2x)%R = 0 = cycle_begin, 所以只需把slow设回head， fast 和 slow 同时往next移动， 两点相遇时即是cycle_begin

public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (true) {
            if (fast == null || fast.next == null) return null;
            // 先move，再check是否相等，因为initially都指向head 一定相等
            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow) break;
            
        }
        slow = head;
        while (slow != fast){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}
