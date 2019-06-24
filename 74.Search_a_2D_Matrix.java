class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        int row = matrix.length;
        int col = matrix[0].length;
        int start = 0;
        int end = row*col-1;
        int mid;
        while (start+1 < end) {
            mid = (start+end)/2;
            if (matrix[mid/col][mid%col] == target) return true;
            if (matrix[mid/col][mid%col] > target) end = mid;
            else start = mid;
        }
        if (matrix[start/col][start%col] == target || matrix[end/col][end%col] == target)
            return true;
        else return false;
    }
}
