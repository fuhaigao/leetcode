class Solution {
    public int titleToNumber(String s) {
        int col = 0;
        int pow = 0;
        for (int i=s.length()-2; i>=0; i--){
            pow++;
            int val = s.charAt(i)- 'A' + 1;
            col += val*Math.pow(26,pow);
        }
        col += s.charAt(s.length()-1) - 'A'+1;
        return col;
    }
}
