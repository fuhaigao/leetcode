class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        // 这里res用 HashSet 为了防止同样的subString被加入多次
        HashSet<String> res = new HashSet();
        HashSet<String> seen = new HashSet();
        for (int i=0; i<s.length()-9; i++) {
            String curr = s.substring(i, i+10);
            // 在 HashSet 里，同样的值只能出现一次，如果add失败 会return false
            if (!seen.add(curr)){
                res.add(curr);
            }
        }
        return new ArrayList(res);
    }
}
