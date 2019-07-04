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
    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode head = sortedArrayToBSTHelper(nums, 0, nums.length-1);
        return head;
    }
    private TreeNode sortedArrayToBSTHelper(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }
        int mid = start + (end - start)/2;     //avoid Integer overflow
        TreeNode curr = new TreeNode(nums[mid]);
        curr.left = sortedArrayToBSTHelper(nums, start, mid-1);
        curr.right = sortedArrayToBSTHelper(nums, mid+1, end);
        return curr;
    }
}
