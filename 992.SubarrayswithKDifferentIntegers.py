class Solution:
    # brute force, TLE
    # def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    #     result = 0
    #     for i in range(1, len(nums)+1):
    #         for j in range(i):
    #             currSet = set(nums[j:i])
    #             if len(currSet) == k:
    #                 result += 1
    #     return result
    
    # Sliding Window 
    # func `atMostKDistanct` calculates the number of subarray with at most k distinct, so result = atMostKDistanct(k) - atMostKDistanct(k-1)
    # 转换成 atMostKDistanct 后，就是经典的 Sliding Window 问题了
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistanct(nums, k) - self.atMostKDistanct(nums,k-1)
    def atMostKDistanct(self, nums, k):
        start, result = 0, 0
        counter = collections.defaultdict(int)
        for i in range(len(nums)):
            counter[nums[i]] += 1
            if counter[nums[i]] == 1:
                k -= 1
            while k < 0:
                counter[nums[start]] -= 1
                if counter[nums[start]] == 0:
                    k += 1
                start += 1
            # print(start, i)
            result += i - start + 1
        return result
        