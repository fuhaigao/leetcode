class Solution {
    // %10 得到last digit
    // /10 move one digit
    // 不用 care 正负号
    // 用 long avoid corner cases
    public int reverse(int x) {
        long res = 0;
        while (x != 0){
            res = res*10 + (x%10);
            x /= 10;
            if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE) return 0;
        }
        return (int)res;
    }
}
