class Solution {
    public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<vector<char>> dictionary(10);
        dictionary[2] = {'a','b','c'};
        dictionary[3] = {'d','e','f'};
        dictionary[4] = {'g','h','i'};
        dictionary[5] = {'j','k','l'};
        dictionary[6] = {'m','n','o'};
        dictionary[7] = {'p','q','r', 's'};
        dictionary[8] = {'t','u','v'};
        dictionary[9] = {'w','x','y','z'};
        
        vector<string> res;
        string curr;
        dfs(dictionary, res, curr, 0, digits);
        return res;
        
    }
    
    void dfs(vector<vector<char>>& dictionary, vector<string>& res, string& curr, int index, string digits) {
        if (index == digits.length()){
            res.push_back(curr);
            return;
        }
        else {
            for (char c : dictionary[digits[index]-'0']){
                curr.push_back(c);
                dfs(dictionary, res, curr, index+1, digits);
                curr.pop_back();
            }
        }
    }
};
