// Create two arrays to map int values and Roman sybols
// Use while loop to check each symbol from the largest to loweset
class Solution {
    public String intToRoman(int num) {
        int[] values = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] strs = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        
        StringBuilder sb = new StringBuilder();
        int index = 0;
        for (int i=0; i<values.length; i++) {
            // use while since multi symbols might be used
            while (num >= values[i]){
                sb.append(strs[i]);
                num -= values[i];
            }
        }
        return sb.toString();
    }
}
