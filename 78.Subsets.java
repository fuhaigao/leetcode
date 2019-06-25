class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList();
        subsetsHelper(res, new ArrayList<Integer>(), nums, 0);
        return res;
    }
    void subsetsHelper(List<List<Integer>> res, List<Integer> curr, int[]nums, int start) {
        res.add(new ArrayList<Integer>(curr));
        for (int i=start; i<nums.length; i++) {
            curr.add(nums[i]);
            subsetsHelper(res, curr, nums, i+1);
            curr.remove(curr.size()-1);
        }
    }
}
