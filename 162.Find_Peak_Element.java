class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0;
        int end = nums.length-1;
        while (start+1 < end) {
            // use mid1 and mid2 to determine increasing or decreasing at mid point
            int mid1 = start + (end-start)/2;
            int mid2 = mid1+1;
            if (nums[mid1] < nums[mid2])
                // values increase at mid point, peek has to be exsited in right part
                start = mid2;
            else
                // values decrease at mid point, peek has to be exsited in left part
                end = mid1;
        }
        if (nums[start] > nums[end]) return start;
        else return end;
    }
}
