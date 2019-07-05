// First, check the four border of the matrix. If there is a element is 'O', alter it and all its neighbor 'O' elements to '1'.

// Then ,alter all the 'O' to 'X'

// At last,alter all the '1' to 'O'


class Solution {
    public void solve(char[][] board) {
        int row = board.length;
        if (row<=1) return;
        int col = board[0].length;
        if (col<=1) return;
        for (int i=0; i<row; i++){
            check(board,i,0);
            check(board,i,col-1);
        }
        for (int j=1; j<col-1; j++){
            check(board, 0, j);
            check(board, row-1, j);
        }
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
                if(board[i][j]=='O')
                    board[i][j]='X';
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
                if(board[i][j]=='1')
                    board[i][j]='O';
        return;
    }
    private void check(char[][]board, int i, int j) {
        if (board[i][j] == 'O') {
            board[i][j] = '1';
            if (i>0) check(board, i-1, j);
            if (j>0) check(board, i, j-1);
            if (i<board.length-1) check(board, i+1, j);
            if (j<board[0].length-1) check(board, i, j+1);
        }
    }
}
