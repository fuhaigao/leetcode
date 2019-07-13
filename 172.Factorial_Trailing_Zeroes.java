class Solution {
    public int trailingZeroes(int n) {
        int count = 0;
        while(n >= 5) {
            int currCount = n/5;
            count+= currCount;
            n = currCount;
        }
        return count;
    }
}
