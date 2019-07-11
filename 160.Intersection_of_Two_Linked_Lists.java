/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // 1. a和b 都从头走到尾
        // 2. a走到尾后从b的开头走，b走到尾后从a的开头走， 这样在第二轮就会在同一起跑线上
        // 3. 当a==b 找到 intersection point，如果没有相交 a == b == null 也出while
        if (headA == null || headB == null) return null;
        ListNode a = headA;
        ListNode b = headB;
        while (a != b) {
            if (a == null) a = headB;
            else a = a.next;
            if (b == null) b = headA;
            else b = b.next;
        }
        return a;
    }
}
