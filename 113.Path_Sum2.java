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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList();
        List<Integer> curr = new ArrayList();
        pathSumHelper(res, curr, root, sum);
        return res;
    }
    
    private void pathSumHelper(List<List<Integer>> res, List<Integer> curr, TreeNode root, int sum) {
        if (root == null ) return;
        curr.add(root.val);
        if (root.left == null && root.right == null && sum == root.val) {
            res.add(new ArrayList(curr));
            curr.remove(curr.size()-1);
            return;
        }
        else {
            pathSumHelper(res, curr, root.left, sum-root.val);
            pathSumHelper(res, curr, root.right, sum-root.val);
            curr.remove(curr.size()-1);
        }
    }
}
