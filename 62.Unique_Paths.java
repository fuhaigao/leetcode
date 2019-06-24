class Solution {
    // sol 1: dp two dimentional
    // public int uniquePaths(int m, int n) {
    //     int [][] res = new int [m][n];
    //     for (int i=0; i<m; i++){
    //         res[i][0] = 1;
    //     }
    //     for (int i=0; i<n; i++){
    //         res[0][i] = 1;
    //     }
    //     for (int i=1; i<m; i++){
    //         for (int j=1; j<n; j++){
    //             res[i][j] = res[i-1][j] + res[i][j-1];
    //         }
    //     }
    //     return res[m-1][n-1];
    // }
    
    // sol 2: dp one dimentional
    // By inspect, each time when we update dp[i][j], we only need dp[i - 1][j] (at the previous row) and dp[i][j - 1] (at the current row). So we can reduce the memory usage to just two rows (O(n))
    // public int uniquePaths(int m, int n) {
    //     int[] prev = new int [m];
    //     int[] curr = new int [m];
    //     for (int i=0; i<m; i++){
    //         prev[i] = 1;
    //         curr[i] = 1;
    //     }
    //     for (int i=1; i<n; i++){
    //         for (int j=1; j<m; j++) {
    //             curr[j] = curr[j-1] + prev[j];
    //         }
    //         prev = curr;
    //     }
    //     return curr[m-1];
    // }
    
    // sol 3: use one array
    // Further inspecting the above code, pre[j] is just the cur[j] before the update. So we can further reduce the memory usage to one row.
    public int uniquePaths(int m, int n) {
        int[] curr = new int [m];
        for (int i=0; i<m; i++){
            curr[i] = 1;
        }
        for (int i=1; i<n; i++){
            for (int j=1; j<m; j++){
                curr[j] += curr[j-1];
            }
        }
        return curr[m-1];
    }
}
