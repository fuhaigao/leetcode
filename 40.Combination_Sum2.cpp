class Solution {
    public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> curr;
        //难点1: 要sort
        sort(candidates.begin(), candidates.end());
        combinationSumHelper(res, candidates, curr, target, 0);
        return res;
    }
    
    void combinationSumHelper(vector<vector<int>>& res, vector<int>& nums, vector<int>& curr, int target, int start){
        if (target == 0){
            res.push_back(curr);
            return;
        }
        else {
            for (int i=start; i<nums.size(); i++){
                //难点2: 要去重
                if (i != start && nums[i] == nums[i-1]) continue;
                if (target >= nums[i]){
                    curr.push_back(nums[i]);
                    combinationSumHelper(res, nums, curr, target-nums[i], i+1);
                    curr.pop_back();
                }
            }
        }
    }
};
