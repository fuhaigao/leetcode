// reverse the number and check with original number
// use long to avoid Integer size overload
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        long reverse = 0;
        int original = x;
        while (x != 0) {
            reverse = reverse*10 + x%10;
            x /= 10;
        }
        if (reverse > Integer.MAX_VALUE) return false;
        if ((int)reverse == original) return true;
        else return false;
    }
}
