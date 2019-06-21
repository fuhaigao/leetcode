class Solution {
    //烦点： int[][] <=> ArrayList
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length <=1 || intervals.length <=1 ) return intervals;
        Arrays.sort(intervals, (a,b) -> a[0]-b[0]);
        ArrayList<int[]> res = new ArrayList<>();
        int[] prev_interval = intervals[0];
        for (int[] curr_interval : intervals) {
            if (curr_interval[0] > prev_interval[1]){
                res.add(prev_interval);
                prev_interval = curr_interval;
            }
            else {
                prev_interval[1] = Math.max(prev_interval[1],curr_interval[1]);
            }
        }
        res.add(prev_interval);
        return res.toArray(new int[res.size()][2]);
    }
}
