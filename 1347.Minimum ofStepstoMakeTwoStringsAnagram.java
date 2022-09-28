class Solution {
    public int minSteps(String s, String t) {
        int[] alph = new int[26];
        for (int i=0; i<s.length(); i++) {
            alph[s.charAt(i) - 'a']++;
            alph[t.charAt(i) - 'a']--;
        }
        int res = 0;
        for (int num : alph) {
            if (num > 0) {
                res += num;
            }
        }
        return res;
    }
}