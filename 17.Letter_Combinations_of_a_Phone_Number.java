// Combination Question
// 1. Create a list to map all numbers to letters
// 2. Use StringBuilder to store current string (store in result)
// 3. To remove last append in SB, use sb.setLength() (实现backtracing 每次的还原)

class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList();
        if (digits == null || digits.length() == 0) return res;
        
        // maping all numbers to letters
        String[] map = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        StringBuilder sb = new StringBuilder();
        helper(res, map, digits, sb, 0);
        return res;
    }
    
    private void helper(List<String> res, String[] map, String digits, StringBuilder curr, int index) {
        if (curr.length() == digits.length()){
            res.add(curr.toString());
            return;
        }
        int mapIndex = digits.charAt(index) - '0';
        for (int i=0; i<map[mapIndex].length(); i++){
            int sbLen = curr.length();
            curr.append(map[mapIndex].charAt(i));
            helper(res, map, digits, curr, index+1);
            curr.setLength(sbLen);
        }
    }
}
