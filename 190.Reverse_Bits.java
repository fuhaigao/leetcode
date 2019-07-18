public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        for (int i=0; i<32; i++) {
            int currEnd = n & 1;    // get the last digit of n
            n >>= 1;                // n right shift 1 digit for next loop
            res <<= 1;              // res left shift for next OR (|)
            res |= currEnd;         // res append curr end digit
            // 最后两步不能反顺序，否则最后res会多shift出一个0
        }
        return res;
    }
}
