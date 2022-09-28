class Solution {
    public int minSteps(String s, String t) {
        int[] alph = new int[26];
        for (int i=0; i<Math.max(s.length(), t.length()); i++) {
            if (i<s.length()) alph[s.charAt(i)-'a']++;
            if (i<t.length()) alph[t.charAt(i)-'a']--;
        }
        int res = 0;
        for (int num : alph) {
            res += Math.abs(num);
        }
        return res;
    }
}