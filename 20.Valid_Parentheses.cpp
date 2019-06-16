class Solution {
    public:
    bool isValid(string s) {
        vector<char> res;
        for (int i=0; i<s.length(); i++){
            if (s[i] == '('){
                res.push_back(')');
            }
            else if (s[i] == '['){
                res.push_back(']');
            }
            else if (s[i] == '{'){
                res.push_back('}');
            }
            else {
                if (res.empty() || res.back() != s[i]) return false;
                res.pop_back();
            }
        }
        return res.empty();
    }
};
