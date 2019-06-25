class Solution {
    public void sortColors(int[] nums) {
        int start = 0, end = nums.length-1, curr = 0;
        while (curr <= end) {
            if (nums[curr] == 0) {
                int tmp = nums[curr];
                nums[curr] = nums[start];
                nums[start] = tmp;
                curr++;
                start++;
            }
            else if (nums[curr] == 2){
                int tmp = nums[curr];
                nums[curr] = nums[end];
                nums[end] = tmp;
                end--;
            }
            else curr++;
        }
    }
}
