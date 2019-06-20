class Solution {
    public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        permutationHelper(res, nums, curr, nums.size());
        return res;
    }
    
    void permutationHelper(vector<vector<int>>& res, vector<int>& nums, vector<int>& curr, int count ){
        if (count == 0){
            res.push_back(curr);
            return;
        }
        else {
            for (int i=0; i<nums.size(); i++){
                if (find(curr.begin(), curr.end(), nums[i]) == curr.end()){
                    // if (!count(curr.begin,curr.end(), nums[i])){
                    curr.push_back(nums[i]);
                    permutationHelper(res, nums, curr, count-1);
                    curr.pop_back();
                }
            }
        }
    }
};
