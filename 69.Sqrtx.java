class Solution {
    public int mySqrt(int x) {
        if (x==0) return 0;
        int start = 1;
        int end = x;
        int mid;
        while (start+1 < end) {
            mid = (start+end)/2;
            if (mid > x/mid) end = mid;
            else if (mid+1 > x/(mid+1)) return mid;
            else start = mid;
        }
        return start;
    }
}
