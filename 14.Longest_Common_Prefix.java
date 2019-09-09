// Initialize first string as prefix
// compare and update prefix with each string
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String prefix = strs[0];
        // compare and update prefix
        for (int i=1; i<strs.length; i++){
            prefix = checkCommonPrefix(prefix, strs[i]);
        }
        return prefix;
    }
    
    // helper function to compare prefix and string
    private String checkCommonPrefix(String prefix, String str) {
        int i = 0;
        StringBuilder sb = new StringBuilder();
        while (i<prefix.length() && i<str.length() && prefix.charAt(i) == str.charAt(i)) {
            sb.append(prefix.charAt(i));
            i++;
        }
        return sb.toString();
    }
}
