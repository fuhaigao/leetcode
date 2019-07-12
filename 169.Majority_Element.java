class Solution {
    // Moore Voting Algorithm
    public int majorityElement(int[] nums) {
        int count = 1;
        int majority = nums[0];
        for (int i=1; i<nums.length; i++) {
            if (nums[i] == majority) count++;
            else {
                count--;
                if (count == 0) {
                    majority = nums[i];
                    count = 1;
                }
            }
        }
        return majority;
    }
    
    // hashmap
    // public int majorityElement(int[] nums) {
    //     Map<Integer, Integer> counter = new HashMap();
    //     for (int num: nums) {
    //         if (!counter.containsKey(num)) counter.put(num,1);
    //         else {
    //             counter.put(num, counter.get(num)+1);
    //         }
    //         if (counter.get(num) > nums.length/2) return num;
    //     }
    //     return -1;
    // }
}
