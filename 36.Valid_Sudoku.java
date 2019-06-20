class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i=0; i<board.length; i++){
            HashSet<Character> row = new HashSet();
            HashSet<Character> col = new HashSet();
            HashSet<Character> square = new HashSet();
            for (int j=0; j<board[0].length; j++){
                if (board[i][j] !='.' && !row.add(board[i][j])) return false;
                if (board[j][i] !='.' && !col.add(board[j][i])) return false;
                
                int row_index = 3*(i/3);
                int col_index = 3*(i%3);
                if (board[row_index+(j/3)][col_index+(j%3)] !='.' && !square.add(board[row_index+(j/3)][col_index+(j%3)]))
                    return false;
            }
        }
        return true;
    }
}



