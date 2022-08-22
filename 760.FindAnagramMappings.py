class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        for i, val in enumerate(nums2):
            d[val].append(i)
        return [d[nums1[i]].pop() for i in range(len(nums1))]
        