// 1. find firstSmall value from the end to start (从后往前第一个比下一个数小的数)
// 2. if firstSmall == -1, means it is already reverse sorted, directly swap all values to get the smallest permutation
// 3. find firstLarge value from the end to start to ensure the next large value is the smallest
// 找firstLarge (比firstSmall大且最小的可能)和firstSmall swap， 同时不能打乱前面的数
// 4. swap the values and then swap the rest
class Solution {
    public void nextPermutation(int[] nums) {
        int firstSmall = -1;
        //从后往前找，因为要保证换完后的值是最小的，比原来大的值
        for (int i=nums.length-2; i>=0; i--){
            if (nums[i] < nums[i+1]){
                firstSmall = i;
                break;
            }
        }
        if (firstSmall == -1){
            int low = 0, high = nums.length-1;
            while (low < high){
                int tmp = nums[low];
                nums[low] = nums[high];
                nums[high] = tmp;
                low++;
                high--;
            }
            return;
        }
        
        //找firstLarge (比firstSmall大且最小的可能)和firstSmall swap， 同时不能打乱前面的数
        int firstLarge = -1;
        
        //此时不用找最小值是因为firstSmall后面的数一定是倒序
        for (int i=nums.length-1; i>=firstSmall; i--){
            if (nums[i] > nums[firstSmall]){
                firstLarge = i;
                break;
            }
        }
        int tmp = nums[firstSmall];
        nums[firstSmall] = nums[firstLarge];
        nums[firstLarge] = tmp;
        
        //sort rest nums
        int low = firstSmall+1;
        int high = nums.length-1;
        while(low < high){
            int temp = nums[low];
            nums[low] = nums[high];
            nums[high] = temp;
            low++;
            high--;
        }
        return;
    }
}
