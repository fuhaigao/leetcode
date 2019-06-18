class Solution {
    public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size()-1;
        int mid;
        while (start+1 < end) {
            mid = (start+end)/2;
            if (nums[mid] == target) return mid;
            if (target < nums[mid]) {
                end = mid;
            }
            else {
                start = mid;
            }
        }
        if (target <= nums[start]) return start;
        else if (target <=nums[end]) return end;
        else return end+1;
    }
};
