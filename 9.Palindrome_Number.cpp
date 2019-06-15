class Solution {
    public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int original = x;
        long reversed  = 0;
        while ( x!=0){
            reversed = reversed*10 + (x%10);
            x /= 10;
            if (reversed > INT_MAX) return false;
        }
        reversed = static_cast<int>(reversed);
        if (reversed == original) return true;
        else return false;
    }
};
