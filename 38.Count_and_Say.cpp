class Solution {
    public:
    string countAndSay(int n) {
        int index = 1;
        string res = "1";
        while (index < n) {
            char curr = res[0];
            int count = 0;
            string curr_str = "";
            for (int i=0; i<res.length(); i++){
                if (res[i] == curr){
                    count++;
                }
                else {
                    curr_str = curr_str + to_string(count) + curr;
                    count = 1;
                    curr = res[i];
                }
            }
            curr_str = curr_str + to_string(count) + curr;
            res = curr_str;
            index++;
        }
        return res;
    }
};
