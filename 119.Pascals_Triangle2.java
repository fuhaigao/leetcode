class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> res = new ArrayList();
        List<Integer> currRow = new ArrayList();
        for (int i=0; i<=rowIndex; i++) {
            currRow.add(0,1);   //当前行的最左边 insert 1
            for (int j=1; j<currRow.size()-1; j++){
                currRow.set(j, currRow.get(j)+currRow.get(j+1));  //更新 2~倒数第二个数
            }
        }
        return currRow;
    }
}
