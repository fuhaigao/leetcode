class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack();
        int tmp = 0;
        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")){
                int right = nums.pop();
                int left = nums.pop();
                if (token.equals("+")) tmp = left + right;
                if (token.equals("-")) tmp = left - right;
                if (token.equals("*")) tmp = left * right;
                if (token.equals("/")) tmp = left / right;
                nums.add(tmp);
            }
            else {
                nums.add(Integer.valueOf(token));
            }
        }
        return nums.pop();
    }
}
