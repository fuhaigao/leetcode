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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTreeHelper(0,0,inorder.length-1, preorder,inorder);
    }
    
    private TreeNode buildTreeHelper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder) {
        // #end condition:
        if (preStart >= preorder.length || inStart > inEnd) return null;
        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = 0;
        //for loop 找inoder index for current root
        for (int i=inStart; i<=inEnd; i++) {
            if (inorder[i] == preorder[preStart]){
                inIndex = i;
                break;
            }
        }
        // left start = preStart + 1
        root.left = buildTreeHelper(preStart+1, inStart, inIndex-1, preorder, inorder);
        // right start = preStart + number of left nodes = preStart + (inIndex - inStart)+1
        root.right = buildTreeHelper(preStart+inIndex-inStart+1, inIndex+1, inEnd, preorder, inorder);
        return root;
    }
}
