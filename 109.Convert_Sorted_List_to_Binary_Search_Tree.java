/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        return sortedListToBSTHelper(head, null);
    }
    private TreeNode sortedListToBSTHelper(ListNode head, ListNode tail) {
        if (head == tail) return null;
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != tail && fast.next != tail) {
            slow = slow.next;
            fast = fast.next.next;
        }
        TreeNode curr = new TreeNode(slow.val);
        curr.left = sortedListToBSTHelper(head, slow);
        curr.right = sortedListToBSTHelper(slow.next, tail);
        return curr;
    }
}
