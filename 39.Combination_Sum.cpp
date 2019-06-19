class Solution {
    public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> curr;
        combinationSumHelper(res, candidates, curr, target, 0);
        return res;
    }
    
    void combinationSumHelper(vector<vector<int>>& res, vector<int>& nums, vector<int>& curr, int target, int index){
        if (target == 0){
            res.push_back(curr);
            return;
        }
        else {
            for (int i=index; i<nums.size(); i++){
                if (target >= nums[i]){
                    curr.push_back(nums[i]);
                    combinationSumHelper(res, nums, curr, target-nums[i], i);
                    curr.pop_back();
                }
            }
        }
    }
};
