class Solution {
    public void setZeroes(int[][] matrix) {
        boolean frZero = false;
        boolean fcZero = false;
        // 每次查到 matrix[i][j] == 0, 把对应的第一行&第一列的数设为0，来代表这一行&这一列要变成0.（这样不会影响到后续的遍历）
        // 考虑到special case: 在第一行/第一列时，会出现问题。 所以用2个bool来 keep track 第一行／第一列是否要变成0
        for (int i=0; i<matrix.length; i++) {
            for (int j=0; j<matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    if (i == 0) frZero = true;
                    if (j == 0) fcZero = true;
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        for (int i=1; i<matrix.length; i++) {
            for (int j=1; j<matrix[0].length; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
        
        if (frZero) {
            for (int j=0; j<matrix[0].length; j++){
                matrix[0][j] = 0 ;
            }
        }
        
        if (fcZero) {
            for (int i=0; i<matrix.length; i++){
                matrix[i][0] = 0;
            }
        }
    }
}
