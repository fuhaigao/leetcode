class Solution {
    public:
    string longestPalindrome(string s) {
        if (s.length() == 0) return s;
        vector<vector<bool>> dp(s.length(), vector<bool>(s.length(), false));
        int max = 0;
        string res = "";
        for (int j=0; j<s.length(); j++){
            for (int i=0; i<=j; i++){
                dp[i][j] = s[i] == s[j] && (j-i<=1 || dp[i+1][j-1]);
                if (dp[i][j]){
                    if((j-i+1) > max){
                        max = j-i+1;
                        res = s.substr(i,j-i+1);
                    }
                }
            }
        }
        return res;
    }
};
