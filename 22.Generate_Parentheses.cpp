class Solution {
    public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string s = "";
        generateParenthesisHelper(res, s, n, n);
        return res;
    }
    
    void generateParenthesisHelper(vector<string>& res, string s, int left, int right){
        if (left > right) return;     //invalid parenthesis
        if (left==0 && right==0 ){
            res.push_back(s);
            return;
        }
        if (left > 0)
        generateParenthesisHelper(res, s+"(", left-1, right);
        if (right > 0)
        generateParenthesisHelper(res, s+")", left, right-1);
    }
};
