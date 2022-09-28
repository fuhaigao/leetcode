class Solution {
    public int calculate(String s) {
        int constantSum = 0, coeffSum = 0, tmpSum = 0, num = 0;
        char lastSign = "+";
        boolean isCoeff = false;
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) num = num*10 + c -'0';
            if (i == s.length()-1 || !Character.isDigit(c)) {
                if (lastSign == '+') {
                    if (isCoeff) coeffSum += tmpSum;
                    else constantSum += tmpSum;
                    tmpSum = num;
                    isCoeff = false;
                } else if (lastSign == '-') {
                    if (isCoeff) coeffSum -= tmpSum;
                    else constantSum -= tmpSum;
                    tmpSum = num;
                    isCoeff = false;
                } else if (lastSign == '*') {
                    tmpSum *= num;
                } else if (lastSign == '/') {
                    tmpSum /= num;
                } else {
                    isCoeff = true;
                }
                lastSign = c;
                num = 0;
            }
        }
        if (isCoeff) coeffSum += tmpSum;
        else constantSum += tmpSum;
        System.out.println(String.valueOf(coeffSum));
        System.out.println(String.valueOf(constantSum));
        return coeffSum;
    }
}