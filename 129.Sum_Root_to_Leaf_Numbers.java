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
    public int sumNumbers(TreeNode root) {
        return sumNumbersHelper(root, 0);
    }
    private int sumNumbersHelper(TreeNode root, int currSum){
        if (root == null) return 0;
        currSum = currSum*10 + root.val;
        if (root.left == null && root.right == null) return currSum;
        return sumNumbersHelper(root.left, currSum) + sumNumbersHelper(root.right, currSum);
    }
}
