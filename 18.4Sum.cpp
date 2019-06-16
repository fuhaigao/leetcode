class Solution {
    public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if (nums.size() < 4) return res;
        sort(nums.begin(), nums.end());
        
        for (int i=0; i<nums.size()-3; i++){
            if (i>0 && nums[i-1] == nums[i]) continue;
            for (int j=i+1; j<nums.size()-2; j++){
                if (j>i+1 && nums[j-1] == nums[j]) continue;
                int start = j+1;
                int end = nums.size()-1;
                while (start < end) {
                    int sum = nums[i] + nums[j] + nums[start] + nums[end];
                    if (sum < target){
                        start++;
                    }
                    else if (sum > target){
                        end--;
                    }
                    else {
                        res.push_back({nums[i], nums[j], nums[start], nums[end]});
                        while (start<end && nums[start] == nums[start+1]) start++;
                        while (start<end && nums[end] == nums[end-1]) end--;
                        start++;
                        end--;
                        
                    }
                }
            }
        }
        return res;
    }
};
