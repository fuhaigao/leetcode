class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int rowMin = 0;
        int colMin = 0;
        int rowMax = n-1;
        int colMax = n-1;
        int curr = 1;
        while (curr<=n*n) {
            for (int i=colMin; i<=colMax; i++)  res[rowMin][i] = curr++;
            rowMin++;
            for (int i=rowMin; i<=rowMax; i++)  res[i][colMax] = curr++;
            colMax--;
            for (int i=colMax; i>=colMin; i--)  res[rowMax][i] = curr++;
            rowMax--;
            for (int i=rowMax; i>=rowMin; i--)  res[i][colMin] = curr++;
            colMin++;
        }
        return res;
    }
}
