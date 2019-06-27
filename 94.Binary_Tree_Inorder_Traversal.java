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
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> node_stack = new Stack();
        List<Integer> res = new ArrayList();
        TreeNode curr = root;
        while (curr != null || !node_stack.empty()) {
            while (curr != null) {
                node_stack.add(curr);
                curr = curr.left;
            }
            curr = node_stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}
