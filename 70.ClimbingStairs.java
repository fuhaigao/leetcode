class Solution {
    // Space can be optimized
    // public int climbStairs(int n) {
    //     int[] dp = new int[n+1];
    //     dp[0] = 1;
    //     dp[1] = 1;
    //     for (int i=2; i<n+1; i++) {
    //         dp[i] = dp[i-1] + dp[i-2];
    //     }
    //     return dp[n];
    // }
    
    public int climbStairs(int n) {
        int a = 1;
        int b = 1;
        for (int i=2; i<n+1; i++) {
            int sum = a+b;
            a = b;
            b = sum;
        }
        return b;
    }
    
    
}