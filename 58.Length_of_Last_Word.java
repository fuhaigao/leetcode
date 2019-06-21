class Solution {
    public int lengthOfLastWord(String s) {
        if (s == null || s.length() == 0) return 0;
        int end = s.length()-1;
        while (end>=0 && s.charAt(end) == ' ') end--;
        if (end<0) return 0;
        int len = 0;
        while (end>=0 && s.charAt(end) != ' ') {
            len++;
            end--;
        }
        return len;
    }
}
