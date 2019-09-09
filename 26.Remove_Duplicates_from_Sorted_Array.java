// 在nums的基础上改数字
// 遇见return 个数，同时改变原数组的题：
// keep a counter for number of valid numbers, change the number at index at same time
class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1;
        for (int i=1; i<nums.length; i++){
            if (nums[i] != nums[i-1]){
                nums[count] = nums[i];
                count++;
            }
        }
        return count;
    }
}
