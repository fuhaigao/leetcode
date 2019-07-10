class Solution {
    // Method 1: Use StringBuilder, trim(), split
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        String[] words = s.trim().split("\\s+");    // \\s 代表 空格或回车   \\s+ 代表多个
        for (int i=words.length-1; i>=0; i--){
            sb.append(words[i] + " ");
        }
        return sb.toString().trim();
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
    
    // Method 2: Not use trim, split
    public String reverseWords(String s) {
        if (s == null || s.length() == 0) return s;
        StringBuilder sb = new StringBuilder();
        int index = s.length()-1;
        while (index>=0) {
            if (s.charAt(index) == ' '){
                index--;
                continue;
            }
            int count = index;
            while (count>=0 && s.charAt(count) != ' ') count--;
            sb.append(s.substring(count+1, index+1));
            sb.append(' ');
            index = count-1;
        }
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
}
