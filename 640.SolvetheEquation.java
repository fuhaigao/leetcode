class Solution {
    public String solveEquation(String equation) {
        String[] equations = equation.split("=");
        int[] left = evaluate(equations[0]);
        int[] right = evaluate(equations[1]);
        int k1 = left[0], b1 = left[1];
        int k2 = right[0], b2 = right[1];
        System.out.println(String.valueOf(k1) + " " + String.valueOf(b1) + " " + String.valueOf(k2) + " " + String.valueOf(b2));
        if (k1 != k2 && b1 != b2) {
            return "x=" + String.valueOf((b2-b1)/(k1-k2));
        } else if (k1 == k2 && b1 == b2) {
            return "Infinite solutions";
        } else if (b1 != b2) {
            return "No solution";
        } else {
            return "x=0";
        }
    }
    
    private int[] evaluate(String equation) {
        int coef = 0, constant = 0, val = 0, plus = 1;
        for (int i=0; i<equation.length()+1; i++) {
            char curr;
            if (i == equation.length()) {
                curr = '+';
            } else {
                curr = equation.charAt(i);
            }
            if (curr == 'x') {
                continue;
            } else if (Character.isDigit(curr)) {
                val = val*10 + Character.getNumericValue(curr);
            } else {
                if (i>0) {
                   if (equation.charAt(i-1) == 'x') {
                        coef += (i>1 && Character.isDigit(equation.charAt(i-2))) ? plus*val : plus*1;
                    } else {
                        constant += plus*val;
                    } 
                }
                
                if (curr == '+') plus = 1;
                else plus = -1;
                val = 0;
            }
        }
        return new int[]{coef, constant};
    }
}java