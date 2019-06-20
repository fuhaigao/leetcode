class Solution {
    public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        vector<bool> used = vector<bool>(nums.size(),false);
        sort(nums.begin(), nums.end());
        permuteUniqueHelper(res,curr,nums,used);
        return res;
    }
    
    void permuteUniqueHelper(vector<vector<int>>& res, vector<int>& curr, vector<int>& nums, vector<bool>& used){
        if (curr.size() == nums.size()){
            res.push_back(curr);
            return;
        }
        for (int i=0; i<nums.size(); i++) {
            if (used[i] || (i>0 && nums[i] == nums[i-1] && !used[i-1])) continue;
            curr.push_back(nums[i]);
            used[i] = true;
            permuteUniqueHelper(res, curr, nums, used);
            used[i] = false;
            curr.pop_back();
        }
    }
};
