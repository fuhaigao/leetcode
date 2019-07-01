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
