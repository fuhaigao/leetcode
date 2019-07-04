class Solution {
    public:
    void nextPermutation(vector<int>& nums) {
        if (nums.empty()) return;
        int firstSmall = -1;
        int index_firstSmall;
        
        //从后往前找，因为要保证换完后的值是最小的，比原来大的值
        for (int i=nums.size()-2; i>=0; i--){
            if (nums[i] < nums[i+1]){
                firstSmall = i;
                break;
            }
        }
        
        //nums 倒序
        if (firstSmall == -1){
            int high = nums.size()-1;
            int low = 0;
            while (low < high){
                int tmp = nums[low];
                nums[low] = nums[high];
                nums[high] = tmp;
                low++;
                high--;
            }
            return;
        }
        else {
            //找firstLarge (比firstSmall大且最小的可能)和firstSmall swap， 同时不能打乱前面的数
            int firstLarge = -1;
            //此时不用找最小值是因为firstSmall后面的数一定是倒序
            for (int i=nums.size()-1; i>firstSmall; i--){
                if (nums[i] > nums[firstSmall]){
                    firstLarge = i;
                    break;
                }
            }
            int tmp = nums[firstSmall];
            nums[firstSmall] = nums[firstLarge];
            nums[firstLarge] = tmp;
            //sort rest nums
            int high = nums.size()-1;
            int low = firstSmall+1;
            while(low < high){
                int tmp = nums[low];
                nums[low] = nums[high];
                nums[high] = tmp;
                low++;
                high--;
            }
            return;
        }
    }
    
};
