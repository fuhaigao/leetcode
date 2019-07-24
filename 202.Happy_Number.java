class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> exist = new HashSet();
        while (exist.add(n)) {
            int squareSum = 0;
            while (n != 0){
                squareSum += Math.pow(n%10, 2);
                n /= 10;
            }
            if (squareSum == 1)
                return true;
            n = squareSum;
        }
        return false;
    }
}
