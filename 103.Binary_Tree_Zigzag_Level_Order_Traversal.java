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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList();
        Queue<TreeNode> queue = new LinkedList();
        
        if (root == null) return res;
        queue.offer(root);
        int order = -1;
        while (!queue.isEmpty()) {
            order *= -1;
            List<Integer> currLevel = new ArrayList();
            int levelNum = queue.size();
            for (int i=0; i<levelNum; i++) {
                if (queue.peek().left != null) queue.offer(queue.peek().left);
                if (queue.peek().right != null) queue.offer(queue.peek().right);
                currLevel.add(queue.poll().val);
            }
            if (order == -1) Collections.reverse(currLevel);
            res.add(currLevel);
        }
        return res;
    }
}
