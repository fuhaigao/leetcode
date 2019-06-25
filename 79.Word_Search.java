class Solution {
    // 难点：如何不用visited[][] 来防止来回check. EX. "aba"
    // 当前字母合格时 设为‘*’，最后再改回去
    // Time Complexity: M*N*4^L
    public boolean exist(char[][] board, String word) {
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                if (existHelper(board, i, j, word, 0))
                    return true;
            }
        }
        return false;
    }
    
    boolean existHelper(char[][]board, int row, int col, String word, int index) {
        if (index == word.length()) return true;
        if (row < 0 || col < 0 || row >=  board.length || col >= board[0].length || board[row][col] != word.charAt(index)) return false;
        board[row][col] = '*';
        boolean res = (existHelper(board, row+1, col, word, index+1) ||
                       existHelper(board, row-1, col, word, index+1) ||
                       existHelper(board, row, col+1, word, index+1) ||
                       existHelper(board, row, col-1, word, index+1));
        board[row][col] = word.charAt(index);
        return res;
    }
}
