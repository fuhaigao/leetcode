class Solution {
    public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty()) return {-1, -1};
        int first = findFirst(nums, target);
        if (first == -1) return {-1, -1};
        int last = findLast(nums, target);
        return {first, last};
    }
    
    int findFirst(vector<int>& nums, int target){
        int start = 0;
        int end = nums.size()-1;
        int mid;
        while (start+1 < end){
            cout << start << " " << end << endl;
            mid = (start+end)/2;
            if (nums[mid] < target){
                start = mid;
            }
            else {
                end = mid;
            }
        }
        if (nums[start] != target && nums[end] != target) return -1;
        if (nums[start] == target) return start;
        else return end;
    }
    
    int findLast(vector<int>& nums, int target){
        int start = 0;
        int end = nums.size()-1;
        while (start+1 < end){
            int mid = (start+end)/2;
            if (nums[mid] > target){
                end = mid;
            }
            else {
                start = mid;
            }
        }
        if (nums[start] != target && nums[end] != target) return -1;
        if (nums[end] == target) return end;
        else return start;
    }
};
