class Solution:
    # dp
    def combinationSum4(self, nums: List[int], target: int) -> int:
        comb = [0] * (target+1)
        comb[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    comb[i] += comb[i-num]
        
        return comb[target]