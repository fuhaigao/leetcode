//The idea is very simple:
//
//1. last bit of (odd number & even number) is 0.
//2. when m != n, There is at least an odd number and an even number, so the last bit position result is 0.
//3. Move m and n rigth a position.
//Keep doing step 1,2,3 until m equal to n, use a factor to record the iteration time.

class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int index = 0;
        while (m != n){
            m >>= 1;
            n >>= 1;
            index++;
        }
        return m << index;
    }
}
