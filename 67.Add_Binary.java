class Solution {
    public String addBinary(String a, String b) {
        int a_end = a.length()-1;
        int b_end = b.length()-1;
        int carry = 0;
        StringBuilder sb = new StringBuilder();
        while (a_end >= 0 || b_end >= 0) {
            int sum = carry;
            if (a_end >= 0) {
                sum += Character.getNumericValue(a.charAt(a_end));
                a_end--;
            }
            if (b_end >= 0) {
                sum += Character.getNumericValue(b.charAt(b_end));
                b_end--;
            }
            carry = sum/2;
            sb.append(sum%2);
        }
        if (carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }
}
