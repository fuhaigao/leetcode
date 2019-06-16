class Solution {
    public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return {};
        string prefix = strs[0];
        for (int i=1; i<strs.size(); i++){
            prefix = helper(prefix, strs[i]);
        }
        return prefix;
    }
    
    string helper(string prefix, string str) {
        string res;
        int index = 0;
        while (prefix[index] == str[index] && index<prefix.length() && index<str.length()){
            res += prefix[index];
            index++;
        }
        return res;
    }
};
