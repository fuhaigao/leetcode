// combination question
// Use two parameters: 'left' for '(', 'right' for ')'
// have a check (right < left) for invalid Parentheses
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList();
        if (n == 0 )return res;
        helper(res, "", n, n);
        return res;
    }
    
    private void helper(List<String> res, String curr, int left, int right){
        // invalid Parentheses, directly return;
        if (right < left) return;
        if (left == 0 && right == 0){
            res.add(curr.toString());
            return;
        }
        if (left > 0)
            helper(res, curr+"(", left-1, right);
        if (right > 0)
            helper(res, curr+")", left, right-1);
    }
}
