class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) 
            return false;
        Map<Character, Character>hm = new HashMap();
        Map<Character, Character>hm2 = new HashMap();
        for (int i=0; i<s.length(); i++) {
            if ((hm2.containsKey(t.charAt(i)) && hm2.get(t.charAt(i)) != s.charAt(i)) || hm.containsKey(s.charAt(i)) && hm.get(s.charAt(i)) != t.charAt(i))
                return false;
            hm.put(s.charAt(i), t.charAt(i));
            hm2.put(t.charAt(i), s.charAt(i));
        }
        return true;
    }
    
    // public boolean isIsomorphic (String s, String t) {
    //     int[] m1 = new int[256];
    //     int[] m2 = new int[256];
    //     int n = s.length();
    //     for (int i = 0; i < n; i++) {
    //         if (m1[s.charAt(i)] != m2[t.charAt(i)]) return false;
    //         m1[s.charAt(i)] = i + 1;
    //         m2[t.charAt(i)] = i + 1;
    //     }
    //     return true;
    // }
}