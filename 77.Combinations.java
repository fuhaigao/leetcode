class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList();
        List<Integer> curr = new ArrayList();
        combinationsHelper(res, curr, n, k, 1);
        return res;
    }
    void combinationsHelper(List<List<Integer>> res, List<Integer> curr, int n, int target, int index) {
        if (target == 0) {
            res.add(new ArrayList<Integer>(curr));
            return;
        }
        else {
            for (int i=index; i<=n; i++){
                curr.add(i);
                combinationsHelper(res, curr, n, target-1, i+1);
                curr.remove(curr.size()-1);
            }
        }
    }
}
