class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        for (int i=1; i<strs.length; i++) {
            prefix = getPrefix(prefix, strs[i]);
        }
        return prefix;
    }
    
    private String getPrefix(String s1, String s2) {
        int idx = 0;
        while (idx < s1.length() && idx < s2.length()) {
            if (s1.charAt(idx) != s2.charAt(idx)) {
                return s1.substring(0, idx);
            }
            idx += 1;
        }
        return s1.substring(0, idx);
    }
}