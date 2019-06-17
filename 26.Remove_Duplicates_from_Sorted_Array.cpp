class Solution {
    public:
    //for loop 从index=1开始，每次跟前一个比。（当一个数第一次出现时，直接count++
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int count = 1;
        for (int i=1; i<nums.size(); i++){
            if (nums[i] != nums[i-1]){
                nums[count] = nums[i];
                count++;
            }
        }
        return count;
    }
};
