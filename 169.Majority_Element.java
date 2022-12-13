public class Solution {
    public int majorityElement(int[] num) {

        int major=num[0], count = 1;
        for(int i=1; i<num.length;i++){
            if(count==0){
                count++;
                major=num[i];
            }else if(major==num[i]){
                count++;
            }else count--;
            
        }
        return major;
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
