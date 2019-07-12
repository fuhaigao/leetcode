class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        int maxLength = Math.max(v1.length, v2.length);
        for (int i=0; i<maxLength; i++) {
            int val1 = 0, val2 = 0;
            if (i < v1.length) val1 = Integer.valueOf(v1[i]);
            if (i < v2.length) val2 = Integer.valueOf(v2[i]);
            
            if (val1 > val2) return 1;
            else if (val1 < val2) return -1;
            else continue;
        }
        return 0;
    }
}
