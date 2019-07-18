public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            int curr = n & 1;
            if (curr == 1) count++;
            n >>>= 1;
            // use >>> for unsigned extension (while >> is signed extension)
        }
        return count;
    }
}
