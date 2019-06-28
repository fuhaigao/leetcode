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
    public List<TreeNode> generateTrees(int n) {
        if (n==0) return new ArrayList();
        return generateTreesHelper(1,n);
    }
    private List<TreeNode> generateTreesHelper (int start, int end) {
        List<TreeNode> list = new ArrayList();
        if (start > end) {
            list.add(null);
            return list;
        }
        for (int root=start; root<=end; root++) {
            List<TreeNode> leftList = generateTreesHelper(start,root-1);
            List<TreeNode> rightList = generateTreesHelper(root+1, end);
            for (TreeNode left : leftList) {
                for (TreeNode right : rightList) {
                    TreeNode curr = new TreeNode(root);
                    curr.left = left;
                    curr.right = right;
                    list.add(curr);
                }
            }
        }
        return list;
    }
}
