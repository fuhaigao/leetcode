class Solution {
    //Space: On^2
    public int minimumTotal(List<List<Integer>> triangle) {
        //[2]
        //[3],[4]
        //[6],[5],[7]
        //[4],[1],[8],[3]
        // dp[i][j] 代表从最顶点到i行j列的最小值
        // relation: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])+triangle[i-1][j-1] (因为triangle starts with triangle[0][0])
        // ex. 5从min(3,4)得到 所以是 min(dp[i-1][j], dp[i-1][j-1])
        int size = triangle.size();
        int[][] dp = new int[size+1][size+1];
        // declare dp 时， size+1， 就可以直接从第一个element开始 方便表示
        for (int i=1; i<=size; i++) {
            for (int j=1; j<=i; j++) {  //第一行只能有一个， 第二行只有两个...
                dp[i][j] = triangle.get(i-1).get(j-1);
                if (i==1 && j==1) continue;    //在triangle顶点时
                else if (j==1) dp[i][j] += dp[i-1][j];  //在第一列时， 不存在dp[i-1][j-1]
                else if (j==i) dp[i][j] += dp[i-1][j-1]; //在每一行的最后一列时， 不存在dp[i-1][j]
                else dp[i][j] += Math.min(dp[i-1][j], dp[i-1][j-1]);
            }
        }
        int min = Integer.MAX_VALUE;
        for (int i=1; i<=size; i++){
            if (dp[size][i]<min) min = dp[size][i];
        }
        return min;
    }
    
    //Update values in given triangle, no extra space
    // public int minimumTotal(List<List<Integer>> triangle) {
    //     int n = triangle.size();
    //     for (int i=0; i<n; i++) {
    //         for (int j=0; j<=i; j++) {
    //             int sum = triangle.get(i).get(j);
    //             if (i==0 && j==0) continue;
    //             if (j==0) sum += triangle.get(i-1).get(j);
    //             else if (j==i) sum += triangle.get(i-1).get(j-1);
    //             else sum += Math.min(triangle.get(i-1).get(j), triangle.get(i-1).get(j-1));
    //             triangle.get(i).set(j,sum);
    //         }
    //     }
    //     int min = Integer.MAX_VALUE;
    //     for (int i=0; i<n; i++){
    //         if (triangle.get(n-1).get(i) < min) min = triangle.get(n-1).get(i);
    //     }
    //     return min;
    // }
}
