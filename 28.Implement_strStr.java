// Use substring function to check if needle included in haystack
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        // for loop condition is <=, since substring 2nd parameteris not included
        for (int i=0; i<=haystack.length()-needle.length(); i++){
            if (haystack.substring(i,i+needle.length()).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}
