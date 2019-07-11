class Solution {
    // 左右双指针find target
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        int begin = 0;
        int end = numbers.length-1;
        while (begin < end){
            long val = numbers[begin] + numbers[end];
            // long val = (long)numbers[begin] + (long)numbers[end];
            if (val == target){
                res[0] = begin+1;
                res[1] = end+1;
                return res;
            }
            if (val < target) begin++;
            else end--;
        }
        return res;
    }
}
