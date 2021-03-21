class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        res = 0
        for num in nums:
            if num not in map.keys():
                left_length = map.get(num-1, 0)
                right_length = map.get(num+1, 0)
                merged_length = left_length + right_length + 1
                res = max(res, merged_length)
                map[num] = merged_length
                #update boundaries
                map[num-left_length] = merged_length
                map[num+right_length] = merged_length
        return res