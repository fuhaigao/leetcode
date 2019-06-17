class Solution {
    public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> values;
        int res = 0;
        int start = 0;
        
        for(int i=0; i<s.length(); i++){
            
            if (values.count(s[i])){
                start = max(start, values.at(s[i])+1);
            }
            values[s[i]] = i;
            res = max(res, i-start+1);
        }
        return res;
    }
};
