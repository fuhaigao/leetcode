class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        res = []
        for num in nums1:
            dict[num] = dict.get(num, 0) + 1
        for num in nums2:
            if num in dict.keys() and dict[num] > 0:
                res.append(num)
                dict[num] -= 1
        return res