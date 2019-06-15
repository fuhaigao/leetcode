class Solution {
    public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, int> values;
        vector<vector<string>> res;
        for (string str: strs){
            vector<int> count(26);
            for (char letter : str){
                count[letter-'a']++;
            }
            string map_key = "";
            for (int i=0; i<26; i++){
                if (count[i] != 0){
                    map_key = map_key + to_string(count[i]) + static_cast<char>(i+'a');
                }
            }
            if(values.count(map_key)){
                res[values.at(map_key)].push_back(str);
            }
            else{
                vector<string> sorted_string;
                sorted_string.push_back(str);
                res.push_back(sorted_string);
                values.insert({map_key, res.size()-1});
            }
        }
        return res;
    }
};
