/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
    private Stack<TreeNode> stack = new Stack();
    
    public BSTIterator(TreeNode root) {
        pushAllLeft(root);
    }
    
    /** @return the next smallest number */
    public int next() {
        TreeNode curr = stack.pop();
        pushAllLeft(curr.right);
        return curr.val;
        
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if (stack.isEmpty()) return false;
        return true;
    }
    
    private void pushAllLeft(TreeNode root) {
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
