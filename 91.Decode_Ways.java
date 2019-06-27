// if s[i-1] == 0 && s[i-2] == 0: return 0
// if s[i-1] == 0: nums[i] = nums[i-2]
// if s[i-2] == 0 || s[i-2] 和 s[i-1]组成的数大于26: nums[i] = nums[i-1]
// else nums[i] = nums[i-1] + nums[i-2]
class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0 || s.charAt(0) == '0') return 0;
        if (s.length() == 1) return 1;
        int prev1 = 1;
        int prev2 = 1;
        
        for (int i=1; i<s.length(); i++) {
            int curr = 0;
            if (!isOneDigitValid(s.charAt(i)) && !isTwoDigitValid(s.charAt(i-1), s.charAt(i))) return 0;
            if (isOneDigitValid(s.charAt(i))) curr += prev1;
            if (isTwoDigitValid(s.charAt(i-1), s.charAt(i))) curr += prev2;
            System.out.println("test: " + prev1 + prev2 + curr);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
    private boolean isOneDigitValid(char c) {
        return c != '0';
    }
    
    private boolean isTwoDigitValid(char prev, char curr) {
        if (prev == '0') return false;
        int val = (prev-'0')*10 + (curr-'0');
        if (val>0 && val<=26) return true;
        return false;
    }
}
