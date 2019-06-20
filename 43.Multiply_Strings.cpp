class Solution {
    public:
    string multiply(string num1, string num2) {
        vector<int> carries = vector<int>(num1.length()+num2.length(), 0);
        string res;
        for (int i=num1.length()-1; i>=0; i--){
            for (int j=num2.length()-1; j>=0; j--){
                //难点
                int product = (num1[i]-'0') * (num2[j]-'0');
                int back_index = i+j+1;
                int front_index = i+j;
                int currSum = product + carries[back_index];
                carries[front_index] += currSum/10;
                carries[back_index] = currSum % 10;
                
            }
        }
        for (int val : carries) {
            cout << res << " " <<  val << endl;
            if (res == "" && val == 0) continue;
            res +=to_string(val);
        }
        if (res == "") res = "0";
        return res;
    }
};
