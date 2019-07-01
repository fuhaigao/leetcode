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
    //BFS
    //     public List<List<Integer>> levelOrderBottom(TreeNode root) {
    //         List<List<Integer>> res = new ArrayList();
    //         if (root == null) return res;
    //         Queue<TreeNode> queue = new LinkedList();
    
    //         queue.offer(root);
    //         while (!queue.isEmpty()) {
    //             int levelNum =  queue.size();
    //             List<Integer> currLevel = new ArrayList();
    //             for (int i=0; i<levelNum; i++){
    //                 if (queue.peek().left != null) queue.offer(queue.peek().left);
    //                 if (queue.peek().right != null) queue.offer(queue.peek().right);
    //                 currLevel.add(queue.poll().val);
    //             }
    //             res.add(0,currLevel);
    //         }
    //         return res;
    //     }
    
    // DFS
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList();
        dfs(res, root, 0);
        return res;
    }
    
    private void dfs(List<List<Integer>> res, TreeNode root, int level) {
        if (root == null) return;
        if (level >= res.size()) res.add(0, new ArrayList());
        res.get(res.size() - level -1).add(root.val);
        dfs(res, root.left, level+1);
        dfs(res, root.right, level+1);
    }
}/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return buildTreeHelper(postorder.length-1, 0, inorder.length-1, inorder, postorder);
    }
    private TreeNode buildTreeHelper(int postEnd, int inStart, int inEnd , int[] inorder, int[] postorder) {
        if (postEnd < 0 || inStart > inEnd ) return null;
        int inIndex = 0;
        TreeNode root = new TreeNode(postorder[postEnd]);
        for (int i=inStart; i<=inEnd; i++) {
            if (inorder[i] == postorder[postEnd]) {
                inIndex = i;
                break;
            }
        }
        // left start = postEnd + number of right nodes = postEnd - (inEnd - inIndex + 1)
        root.left = buildTreeHelper(postEnd-inEnd+inIndex-1, inStart, inIndex-1, inorder, postorder);
        //right start = postEnd + 1
        root.right = buildTreeHelper(postEnd-1, inIndex+1, inEnd, inorder, postorder);
        return root;
    }
}
