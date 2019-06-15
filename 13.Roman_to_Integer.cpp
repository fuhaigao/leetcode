class Solution {
    public:
    int romanToInt(string s) {
        int res = toNumber(s[0]);
        for (int i=1; i<s.length(); i++){
            res += toNumber(s[i]);
            if (toNumber(s[i-1]) < toNumber(s[i])){
                res = res - 2*toNumber(s[i-1]);
            }
        }
        return res;
    }
    
    int toNumber(char roman) {
        switch (roman) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
        }
        return 0;
    }
};
