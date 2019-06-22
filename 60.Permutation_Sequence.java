class Solution {
    public String getPermutation(int n, int k) {
        int []factorial = new int [n+1];
        factorial[0] = 1;
        for(int i=1; i<=n; i++){
            factorial[i] = factorial[i-1]*i;
        }
        // factorial = {1,1,2,6,24,...,n!}
        List<Integer> nums = new ArrayList<>();
        for (int i=1; i<=n; i++){
            nums.add(i);
        }
        // nums = {1,2,3,4,5,...,n}
        StringBuilder sb = new StringBuilder();
        k--;    //since things start at 0
        for (int i=n; i>0; i--){
            int index = k/factorial[i-1];   //求出当前位置应该取第index个数
            sb.append(String.valueOf(nums.get(index)));     //从nums（剩下的数中）找到对应index的数
            nums.remove(index);
            k -= index*factorial[i-1];  //ex：k = 14-2*(1*2*3) = 2
            
        }
        return sb.toString();
    }
}
