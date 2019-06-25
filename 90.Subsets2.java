class Solution {
    // 难点：if (i>start && nums[i] == nums[i-1]) continue;
    // 防止重复
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList();
        subsetsHelper(res, new ArrayList<Integer>(), nums, 0);
        return res;
    }
    void subsetsHelper(List<List<Integer>> res, List<Integer> curr, int[]nums, int start) {
        res.add(new ArrayList<Integer>(curr));
        for (int i=start; i<nums.length; i++) {
            if (i > start && nums[i] == nums[i-1]) continue;
            curr.add(nums[i]);
            subsetsHelper(res, curr, nums, i+1);
            curr.remove(curr.size()-1);
        }
    }
}
