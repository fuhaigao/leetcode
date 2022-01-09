class Solution:
    # sum[i, j] = sum[0, j] - sum[0, i - 1]    --> sum[0, i - 1] = sum[0, j] - sum[i, j]
    # k           sum         hashmap-key      --> hashmap-key   = sum - k
    def subarraySum(self, nums: List[int], k: int) -> int:
        frequency = dict()
        frequency[0] = 1
        sum, result = 0, 0
        for num in nums:
            sum += num
            if sum-k in frequency.keys():
                result += frequency[sum-k]
            frequency[sum] = frequency.get(sum, 0)+1
        return result