class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length;
        int cols = obstacleGrid[0].length;
        int[] curr = new int[cols];
        curr[0] = 1;
        for (int i=0; i<rows; i++){
            for (int j=0; j<cols; j++){
                if (obstacleGrid[i][j] == 1) curr[j] = 0;
                else if (j>0) curr[j] += curr[j-1];
            }
        }
        return curr[cols-1];
    }
}
