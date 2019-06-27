class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList();
        res.add(0);
        for (int i=0; i<n; i++){
            int currSize = res.size();
            for (int j=currSize-1; j>=0; j--){
                int tmp = (1<<i) | res.get(j);
                res.add(tmp);
            }
        }
        return res;
    }
}
