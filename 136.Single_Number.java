// use xor (一样的 return 0， 不一样的 return 1)
// xor(0,0) => 0; xor(1,1) => 0; xor(1,0) => 1; xor(0,1) =>1
/*
 N1 ^ N1 ^ N2 ^ N2 ^..............^ Nx ^ Nx ^ N
 = (N1^N1) ^ (N2^N2) ^..............^ (Nx^Nx) ^ N
 = 0 ^ 0 ^ ..........^ 0 ^ N
 = N
 XOR is commutative
 */

class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for(int i=0; i<nums.length; i++){
            res ^= nums[i];
        }
        return res;
    }
}
