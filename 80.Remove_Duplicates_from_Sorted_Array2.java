class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1;
        int currCount = 1;
        for (int i=1; i<nums.length; i++){
            if (nums[i] == nums[i-1] && currCount >= 2) continue;
            else if (nums[i] != nums[i-1]) {
                currCount = 1;
                nums[count] = nums[i];
                count++;
            }
            else {
                nums[count] = nums[i];
                count++;
                currCount++;
            }
        }
        return count;
    }
}
