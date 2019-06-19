class Solution {
    public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;
        int start = 0;
        int end = nums.size()-1;
        int mid;
        while (start+1 < end){
            mid = (start+end)/2;
            if(target == nums[mid]) return mid;
            if(nums[start] < nums[mid]){
                if (target>=nums[start] && target<nums[mid]) end = mid;
                else start = mid;
            }
            else {
                if(target>nums[mid] && target<=nums[end]) start = mid;
                else end = mid;
            }
        }
        if(nums[start] == target) return start;
        else if (nums[end] == target) return end;
        else return -1;
    }
};
