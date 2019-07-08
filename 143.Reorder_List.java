/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

//知识点1: find mid point of linked list (因为终点是middle of given linkedlist)
//知识点2: reverse a linked list （因为后半部分需要reverse）
//知识点3: 构建新 linkedlist

class Solution {
    public void reorderList(ListNode head) {
        if (head == null) return;
        ListNode mid = findMid(head);
        ListNode l2 = mid.next;
        mid.next = null;
        l2 = reverseList(l2);
        ListNode l1 = head;
        
        // 知识点3: 构建新 linkedlist
        while (l1 != null && l2 != null) {
            ListNode next = l1.next;
            l1.next = l2;
            l2 = l2.next;
            l1.next.next = next;
            l1 = next;
        }
        return;
    }
    
    // 知识点1: find mid point of linked list
    private ListNode findMid(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow =slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
    
    // 知识点2: reverse a linked list
    private ListNode reverseList(ListNode head) {
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }
}
