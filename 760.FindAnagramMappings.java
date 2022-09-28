class Solution {
    public int[] anagramMappings(int[] nums1, int[] nums2) {
        Map<Integer, Stack<Integer>> hm = new HashMap<>();
        for (int i=0; i<nums2.length; i++) {
            int num = nums2[i];
            if (!hm.containsKey(num)) {
                hm.put(num, new Stack<>());
            }
            hm.get(num).push(i);
        }
        int[] res = new int[nums1.length];
        for (int i=0; i<nums1.length; i++) {
            res[i] = hm.get(nums1[i]).pop();
        }
        return res;
        
    }
}