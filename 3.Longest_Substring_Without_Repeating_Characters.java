class Solution {
    // 用 hashMap 存每一个character 对应的index
    // start 更新 start point，当出现重复
    // res 更新目前最长的值
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        Map<Character, Integer> hm = new HashMap();
        int start = 0;
        int res = 0;
        for (int i=0; i<s.length(); i++){
            char curr = s.charAt(i);
            if (hm.containsKey(curr)){
                start = Math.max(start, hm.get(curr)+1);
                // 难点：Ex. abcdecfgah
                // when i=5 (2nd c), start = 3
                // when i=8 (2nd a), start cannot equals to 0+1, should remain as 3
            }
            hm.put(curr, i);
            res = Math.max(res, i-start+1);
        }
        return res;
    }
}
