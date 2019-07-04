class Solution {
    public boolean isPalindrome(String s) {
        int front = 0, end = s.length()-1;
        while (front < end) {
            if (!Character.isLetterOrDigit(s.charAt(front))) front++;
            else if (!Character.isLetterOrDigit(s.charAt(end))) end--;
            else if (Character.toLowerCase(s.charAt(front)) != Character.toLowerCase(s.charAt(end)))
                return false;
            else {
                front++;
                end--;
            }
        }
        return true;
    }
}
