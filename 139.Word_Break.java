// recursion DP
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        // 可不用新存 hashset，只为更快速判断is curr word exist in wordDict
        Set<String> dict = new HashSet<String>(wordDict);
        // 存储看过的sub string true/false
        Map<String, Boolean> mem = new HashMap<String, Boolean>();
        return wordBreakHelper(dict, mem, s);
    }
    private boolean wordBreakHelper(Set<String> dict, Map<String, Boolean> mem, String curr) {
        // two end conditions
        if (dict.contains(curr)) {
            mem.put(curr, true);
            return true;
        }
        if (mem.containsKey(curr)) return mem.get(curr);
        
        for (int i=1; i<curr.length(); ++i) {
            String left = curr.substring(0,i);
            String right = curr.substring(i);
            // 重点：如果一部分在dict里，另一部分call recursion returned true， 直接true
            if (dict.contains(right) && wordBreakHelper(dict,mem,left)) {
                mem.put(curr, true);
                return true;
            }
        }
        mem.put(curr, false);
        return false;
    }
}
