class Solution {
    public:
    int myAtoi(string str) {
        long res = 0;
        int sign = 1;
        int start = 0;
        while (str[start] == ' '){
            start++;
        }
        if (str[start] == '-'){
            sign = -1;
            start++;
        }
        else if (str[start] == '+'){
            sign = 1;
            start++;
        }
        for (int i=start; i<str.length(); i++){
            
            if (!isdigit(str[i])){
                cout << "not a digit" << endl;
                return static_cast<int>(sign*res);
            }
            else {
                cout << str[i] << " " << res << endl;
                res = res*10 + (str[i]-'0');
                if (res > INT_MAX && sign==1) return INT_MAX;
                if (res > INT_MAX && sign==-1) return INT_MIN;
            }
        }
        return static_cast<int>(res*sign);
    }
};
