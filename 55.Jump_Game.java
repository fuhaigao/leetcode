class Solution {
    public boolean canJump(int[] nums) {
        int curr_step = 0;
        int reach = 0;
        while (curr_step <= reach) {
            reach = Math.max(reach, curr_step + nums[curr_step]);
            if (reach >= nums.length-1) return true;
            curr_step++;
        }
        return (reach >= nums.length-1);
    }
}
