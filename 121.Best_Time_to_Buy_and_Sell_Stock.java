class Solution {
    public int maxProfit(int[] prices) {
        int currMax = 0;
        int resMax = 0;
        for (int i=1; i<prices.length; i++) {
            currMax = Math.max(0, currMax + prices[i]-prices[i-1]);
            resMax = Math.max(resMax, currMax);
        }
        return resMax;
    }
    
    //brutal force
    public int maxProfit(int[] prices) {
        int size = prices.length;
        int max = 0;
        for (int i=0; i<size; i++) {
            for (int j=i+1; j<size; j++) {
                max = Math.max(max, prices[j]-prices[i]);
            }
        }
        return max;
    }
}
