class Solution {
    public:
    int divide(int dividend, int divisor) {
        int sign = 1;
        if ((dividend<0 && divisor>0) || (dividend>0 && divisor<0))
        sign = -1;
        long curr_dividend = abs(static_cast<long>(dividend));
        long curr_divisor = abs(static_cast<long>(divisor));
        
        // Ex: 32/3
        // 32/3 => 32/6 => 32/12 => 32/24 => 32/48 X get multiple=4, 剩余32-24=6
        
        long multiple_sum = 0;
        while (curr_dividend >= curr_divisor) {
            long sum = curr_divisor;
            long multiple = 1;
            while ((sum+sum) <= curr_dividend) {
                multiple += multiple;
                sum+=sum;
            }
            multiple_sum += multiple;
            //难点
            curr_dividend = curr_dividend - sum;
        }
        
        int res;
        if (multiple_sum > INT_MAX) {
            res = (sign == 1) ? INT_MAX : INT_MIN;
        } else {
            res = static_cast<int>(multiple_sum)*sign;
        }
        return res;
    }
};
