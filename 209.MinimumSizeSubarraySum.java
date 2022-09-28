class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int curr = 0;
        int minLength = Integer.MAX_VALUE;
        int start = 0;
        for (int i=0; i<nums.length; i++) {
            curr += nums[i];
            while (curr >= target && start<nums.length) {
                minLength = Math.min(minLength, i-start+1);
                curr -= nums[start++];
            }
        }
        return minLength == Integer.MAX_VALUE ? 0 : minLength;
        
    }
}