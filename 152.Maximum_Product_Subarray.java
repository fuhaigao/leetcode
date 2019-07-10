class Solution {
    // dp O(N) space
    // public int maxProduct(int[] nums) {
    //     if (nums == null || nums.length == 0) return 0;
    //     int size = nums.length;
    //     int[] max = new int[size];
    //     int[] min = new int[size];
    //     max[0] = nums[0];
    //     min[0] = nums[0];
    //     int currMax = max[0];
    //     for (int i=1; i<size; i++){
    //         max[i] = Math.max(nums[i], Math.max(max[i-1]*nums[i], min[i-1]*nums[i]));
    //         min[i] = Math.min(nums[i], Math.min(max[i-1]*nums[i], min[i-1]*nums[i]));
    //         currMax = Math.max(currMax, max[i]);
    //     }
    //     return currMax;
    // }
    
    // dp constant space
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int currMax = nums[0];
        int currMin = nums[0];
        int max = nums[0];
        for (int i=1; i<nums.length; i++){
            int nextMax = nums[i]*currMax;
            int nextMin = nums[i]*currMin;
            currMax = Math.max(nums[i], Math.max(nextMax, nextMin));
            currMin = Math.min(nums[i], Math.min(nextMax, nextMin));
            max = Math.max(max,currMax);
        }
        return max;
    }
}
